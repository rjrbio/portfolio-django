from django.db import models
from django.utils.text import slugify

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    slug = models.SlugField(unique=True, blank=True)
    excerpt = models.TextField(max_length=300, verbose_name="Extracto")
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(upload_to='blog/', verbose_name="Imagen destacada", blank=True, null=True)
    published = models.BooleanField(default=True, verbose_name="Publicado")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['-created_at']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
