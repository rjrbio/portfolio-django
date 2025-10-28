from django.db import models

class Technology(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    icon = models.ImageField(upload_to='techs/', verbose_name="Ícono", blank=True, null=True)
    proficiency = models.IntegerField(default=50, verbose_name="Nivel de dominio (%)", help_text="0-100")
    category = models.CharField(max_length=50, verbose_name="Categoría", 
                                 choices=[
                                     ('frontend', 'Frontend'),
                                     ('backend', 'Backend'),
                                     ('database', 'Base de Datos'),
                                     ('tools', 'Herramientas'),
                                     ('other', 'Otros')
                                 ])
    
    class Meta:
        verbose_name = "Tecnología"
        verbose_name_plural = "Tecnologías"
        ordering = ['category', 'name']
    
    def __str__(self):
        return self.name
