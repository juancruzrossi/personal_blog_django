from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name = 'index'),
    path('economia/', economia, name = 'economia'),
    path('programacion/', programacion, name = 'programacion'),
    path('about/', about, name = 'about'),
    path('contacto/', contacto, name = 'contacto'),
    path('<slug:slug>', detallepost, name='detallepost'),
]
