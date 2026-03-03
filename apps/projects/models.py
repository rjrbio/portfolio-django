from django.db import models
from django.utils.text import slugify

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(upload_to='projects/', verbose_name="Imagen", blank=True, null=True)
    url = models.URLField(blank=True, null=True, verbose_name="URL del proyecto")
    github_url = models.URLField(blank=True, null=True, verbose_name="URL de GitHub")
    technologies = models.CharField(max_length=500, verbose_name="Tecnologías usadas", help_text="Separadas por comas")
    featured = models.BooleanField(default=False, verbose_name="Destacado")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ['-created_at']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def get_technologies_list(self):
        """Retorna las tecnologías como una lista"""
        if self.technologies:
            return [tech.strip() for tech in self.technologies.split(',')]
        return []
    
    def __str__(self):
        return self.title
