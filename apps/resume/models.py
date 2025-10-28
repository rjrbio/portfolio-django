from django.db import models

class Education(models.Model):
    institution = models.CharField(max_length=200, verbose_name="Institución")
    degree = models.CharField(max_length=200, verbose_name="Título/Grado")
    field = models.CharField(max_length=200, verbose_name="Campo de estudio")
    start_date = models.DateField(verbose_name="Fecha de inicio")
    end_date = models.DateField(verbose_name="Fecha de fin", blank=True, null=True)
    current = models.BooleanField(default=False, verbose_name="Actualmente estudiando")
    description = models.TextField(verbose_name="Descripción", blank=True)
    
    class Meta:
        verbose_name = "Educación"
        verbose_name_plural = "Educación"
        ordering = ['-start_date']
    
    def __str__(self):
        return f"{self.degree} - {self.institution}"

class Experience(models.Model):
    company = models.CharField(max_length=200, verbose_name="Empresa")
    position = models.CharField(max_length=200, verbose_name="Cargo")
    start_date = models.DateField(verbose_name="Fecha de inicio")
    end_date = models.DateField(verbose_name="Fecha de fin", blank=True, null=True)
    current = models.BooleanField(default=False, verbose_name="Trabajo actual")
    description = models.TextField(verbose_name="Descripción")
    
    class Meta:
        verbose_name = "Experiencia"
        verbose_name_plural = "Experiencias"
        ordering = ['-start_date']
    
    def __str__(self):
        return f"{self.position} en {self.company}"
