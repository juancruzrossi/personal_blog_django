from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Post, Categoria
from django.db.models import Q
from django.core.paginator import Paginator


def home(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True).order_by('-id')
    
    if queryset:
        posts = Post.objects.filter(Q(titulo__icontains = queryset) | Q(descripcion__icontains = queryset)).distinct()
        
    #paginacion
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    
    return render(request, 'index.html', {'posts':posts})


def detallepost(request, slug):

    post = get_object_or_404(Post, slug=slug)

    return render(request, 'post.html', {'detallepost':post})

def economia(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True, 
                                categoria = Categoria.objects.get(nombre__iexact = 'Economía')).order_by('-id')
    
    if queryset:
        posts = Post.objects.filter(Q(titulo__icontains = queryset) | Q(descripcion__icontains = queryset), estado = True, categoria = Categoria.objects.get(nombre__iexact = 'Economía')).distinct()
        
    #paginacion
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    
    return render(request, 'economia.html', {'posts':posts})

def programacion(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True, 
                                categoria = Categoria.objects.get(nombre__iexact = 'Programación')).order_by('-id')
    if queryset:
        posts = Post.objects.filter(Q(titulo__icontains = queryset) | Q(descripcion__icontains = queryset), estado = True, categoria = Categoria.objects.get(nombre__iexact = 'Programación')).distinct()
    
    #paginacion
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    
    return render(request, 'programacion.html', {'posts':posts})

def about(request):
    return render(request, 'about.html')

def contacto(request):

    return render(request, 'contacto.html')