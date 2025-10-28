from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    icon = models.CharField(max_length=100, verbose_name="Ícono (clase CSS)", help_text="Ej: fas fa-code")
    order = models.IntegerField(default=0, verbose_name="Orden")
    
    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        ordering = ['order']
    
    def __str__(self):
        return self.title
