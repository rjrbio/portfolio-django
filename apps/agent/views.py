import json
import openai
from django.conf import settings
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.throttling import AnonRateThrottle

from apps.about.models import About
from .tools import TOOLS, execute_tool


SYSTEM_PROMPT = """Eres el asistente de IA del portafolio de {name}.
Tu misión es ayudar a reclutadores y clientes potenciales a conocer su perfil profesional.

Usa las herramientas disponibles para consultar información actualizada sobre sus proyectos,
habilidades técnicas, experiencia laboral y servicios. No inventes datos.

Sé profesional y conciso. Responde siempre en el mismo idioma que la pregunta."""

MAX_ITERATIONS = 8
AGENT_MODEL = getattr(settings, "OPENAI_AGENT_MODEL", "gpt-4o")
OPENAI_TIMEOUT = float(getattr(settings, "OPENAI_TIMEOUT_SECONDS", 25))


class AgentRateThrottle(AnonRateThrottle):
    scope = 'agent'


@api_view(["POST"])
@throttle_classes([AgentRateThrottle])
def agent_query(request):
    question = request.data.get("question", "").strip()
    if not question:
        return Response(
            {"error": "La pregunta no puede estar vacía."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    api_key = settings.OPENAI_API_KEY
    if not api_key:
        return Response(
            {"error": "El agente no está configurado. Contacta al administrador."},
            status=status.HTTP_503_SERVICE_UNAVAILABLE,
        )

    about = About.objects.first()
    owner_name = about.name if about else "el desarrollador"
    system = SYSTEM_PROMPT.format(name=owner_name)

    client = openai.OpenAI(api_key=api_key)
    messages = [
        {"role": "system", "content": system},
        {"role": "user", "content": question},
    ]

    try:
        for _ in range(MAX_ITERATIONS):
            response = client.chat.completions.create(
                model=AGENT_MODEL,
                messages=messages,
                tools=TOOLS,
                tool_choice="auto",
                timeout=OPENAI_TIMEOUT,
            )

            choice = response.choices[0]

            if choice.finish_reason == "stop":
                return Response({"answer": choice.message.content})

            if choice.finish_reason != "tool_calls":
                break

            # Añadir respuesta del asistente con los tool_calls
            messages.append(choice.message)

            # Ejecutar cada tool call y devolver resultados
            for tool_call in choice.message.tool_calls:
                try:
                    tool_input = json.loads(tool_call.function.arguments)
                except (json.JSONDecodeError, ValueError):
                    tool_input = {}

                result = execute_tool(tool_call.function.name, tool_input)
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": result,
                })

    except openai.AuthenticationError:
        return Response(
            {"error": "API key inválida. Revisa la configuración."},
            status=status.HTTP_503_SERVICE_UNAVAILABLE,
        )
    except openai.RateLimitError:
        return Response(
            {"error": "Límite de uso alcanzado. Intenta en unos minutos."},
            status=status.HTTP_429_TOO_MANY_REQUESTS,
        )
    except openai.APITimeoutError:
        return Response(
            {"error": "El servicio de IA tardó demasiado en responder."},
            status=status.HTTP_504_GATEWAY_TIMEOUT,
        )
    except openai.APIError as exc:
        return Response(
            {"error": f"Error del servicio de IA: {str(exc)}"},
            status=status.HTTP_502_BAD_GATEWAY,
        )

    return Response(
        {"error": "No se pudo completar la consulta."},
        status=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )
