from django.urls import path
from . import views

urlpatterns = [
    path("listar/", views.produtos, name="listar"),
    path("cadastrar/",views.addprodutos),
    path("cadastrar_categoria/",views.addCategorias)
]
