from django.db import models
from ckeditor.fields import RichTextField

class Categoria(models.Model):
    nombre = models.CharField('Nombre de la categoría', max_length=100, null=False, blank=False)
    estado = models.BooleanField('Categoría Activada/Categoría No Activada', default=True)
    fecha_creacion = models.DateField('Fecha De Creación', auto_now=False, auto_now_add=True)
    
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        
    def __str__(self):
        return self.nombre
    

class Autor(models.Model):
    nombres = models.CharField('Nombre de Autor', max_length=255, null=False, blank=False)
    apellidos = models.CharField('Apellido de Autor', max_length=255, null=False, blank=False)
    facebook = models.URLField('Facebook', null=True, blank=True)
    twitter = models.URLField('Twitter', null=True, blank=True)
    instagram = models.URLField('Instagram', null=True, blank=True)
    web = models.URLField('Web', null=True, blank=True)
    correo = models.EmailField('Correo Electrónico', blank=False, null=False)
    estado = models.BooleanField('Autor Activo/No Activo', default=True)
    fecha_creacion = models.DateField('Fecha De Creación', auto_now=False, auto_now_add=True)
    
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        
    
    def __str__(self):
        return f'{self.nombres} {self.apellidos}'
    
    
class Post(models.Model):
    titulo = models.CharField('Título', max_length=100, blank=False, null=False)
    slug = models.CharField('Slug', max_length=100, blank=False, null=False)
    descripcion = models.CharField('Descripción', max_length=100, blank=False, null=False)
    contenido = RichTextField()
    imagen = models.URLField(max_length=255, blank=False, null=False)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    estado = models.BooleanField('Publicado/No Publicado', default=True)
    fecha_creacion = models.DateField('Fecha De Creación', auto_now=False, auto_now_add=True)
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        
    def __str__(self):
        return self.titulo
    
    
    