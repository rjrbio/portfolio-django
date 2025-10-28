from django.db import models

class About(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre completo")
    title = models.CharField(max_length=200, verbose_name="Título profesional")
    bio = models.TextField(verbose_name="Biografía")
    profile_image = models.ImageField(upload_to='about/', verbose_name="Foto de perfil", blank=True, null=True)
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=50, verbose_name="Teléfono", blank=True)
    location = models.CharField(max_length=200, verbose_name="Ubicación", blank=True)
    github = models.URLField(blank=True, verbose_name="GitHub")
    linkedin = models.URLField(blank=True, verbose_name="LinkedIn")
    twitter = models.URLField(blank=True, verbose_name="Twitter")
    cv_file = models.FileField(upload_to='cv/', verbose_name="CV (PDF)", blank=True, null=True)
    
    class Meta:
        verbose_name = "Sobre Mí"
        verbose_name_plural = "Sobre Mí"
    
    def __str__(self):
        return self.name
