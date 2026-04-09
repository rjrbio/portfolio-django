"""
Definición de tools en formato OpenAI y su lógica de ejecución.
Cada tool consulta los modelos de Django y devuelve JSON.
"""
import json

from apps.about.models import About
from apps.projects.models import Project
from apps.resume.models import Education, Experience
from apps.services.models import Service
from apps.techs.models import Technology


# ── Definiciones de tools para la API de OpenAI ───────────────────────────

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_projects",
            "description": (
                "Devuelve los proyectos del portafolio con título, descripción, "
                "tecnologías usadas, URL de demo y enlace a GitHub."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "featured_only": {
                        "type": "boolean",
                        "description": "Si es true, devuelve solo los proyectos destacados.",
                    }
                },
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_skills",
            "description": (
                "Devuelve las habilidades técnicas agrupadas por categoría "
                "(frontend, backend, database, tools, other) con nivel de dominio."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "category": {
                        "type": "string",
                        "description": "Filtrar por categoría. Omitir para todas.",
                        "enum": ["frontend", "backend", "database", "tools", "other"],
                    }
                },
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_experience",
            "description": "Devuelve la experiencia laboral y la formación académica.",
            "parameters": {"type": "object", "properties": {}},
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_about",
            "description": (
                "Devuelve el perfil profesional: nombre, título, biografía, "
                "email, ubicación y redes sociales."
            ),
            "parameters": {"type": "object", "properties": {}},
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_services",
            "description": "Devuelve los servicios profesionales que se ofrecen.",
            "parameters": {"type": "object", "properties": {}},
        },
    },
]


# ── Ejecutores ─────────────────────────────────────────────────────────────

def execute_tool(name: str, tool_input: dict) -> str:
    handlers = {
        "get_projects": _get_projects,
        "get_skills": _get_skills,
        "get_experience": _get_experience,
        "get_about": _get_about,
        "get_services": _get_services,
    }
    handler = handlers.get(name)
    if handler is None:
        return json.dumps({"error": f"Tool desconocida: {name}"})
    return handler(tool_input)


def _get_projects(inp: dict) -> str:
    qs = Project.objects.all()
    if inp.get("featured_only"):
        qs = qs.filter(featured=True)
    data = [
        {
            "title": p.title,
            "description": p.description,
            "technologies": p.get_technologies_list(),
            "url": p.url or "",
            "github_url": p.github_url or "",
            "featured": p.featured,
        }
        for p in qs
    ]
    return json.dumps(data, ensure_ascii=False)


def _get_skills(inp: dict) -> str:
    qs = Technology.objects.all()
    if category := inp.get("category"):
        qs = qs.filter(category=category)
    by_category: dict = {}
    for tech in qs:
        by_category.setdefault(tech.category, []).append(
            {
                "name": tech.name,
                "proficiency": tech.proficiency,
                "icon_class": tech.icon_class,
            }
        )
    return json.dumps(by_category, ensure_ascii=False)


def _get_experience(inp: dict) -> str:
    experience = [
        {
            "company": e.company,
            "position": e.position,
            "start_date": str(e.start_date),
            "end_date": str(e.end_date) if e.end_date else "Actualidad",
            "current": e.current,
            "description": e.description,
        }
        for e in Experience.objects.all()
    ]
    education = [
        {
            "institution": e.institution,
            "degree": e.degree,
            "field": e.field,
            "start_date": str(e.start_date),
            "end_date": str(e.end_date) if e.end_date else "Actualidad",
            "current": e.current,
        }
        for e in Education.objects.all()
    ]
    return json.dumps(
        {"experience": experience, "education": education}, ensure_ascii=False
    )


def _get_about(inp: dict) -> str:
    about = About.objects.first()
    if not about:
        return json.dumps({"error": "No hay información disponible."})
    return json.dumps(
        {
            "name": about.name,
            "title": about.title,
            "bio": about.bio,
            "email": about.email,
            "location": about.location,
            "github": about.github,
            "linkedin": about.linkedin,
        },
        ensure_ascii=False,
    )


def _get_services(inp: dict) -> str:
    data = [
        {"title": s.title, "description": s.description, "icon": s.icon}
        for s in Service.objects.all()
    ]
    return json.dumps(data, ensure_ascii=False)
