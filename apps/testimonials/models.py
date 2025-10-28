from django.db import models

class Testimonial(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre")
    position = models.CharField(max_length=200, verbose_name="Cargo/Posición")
    company = models.CharField(max_length=200, verbose_name="Empresa", blank=True)
    content = models.TextField(verbose_name="Testimonio")
    avatar = models.ImageField(upload_to='testimonials/', verbose_name="Foto", blank=True, null=True)
    rating = models.IntegerField(default=5, verbose_name="Calificación", help_text="1-5 estrellas")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Testimonio"
        verbose_name_plural = "Testimonios"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.company}"
