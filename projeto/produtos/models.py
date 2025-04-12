from django.db import models

class Categoria(models.Model):
    Descricao = models.CharField(max_length=200)

class Produto(models.Model):
    Descricao = models.CharField(max_length=200)
    Referencia = models.CharField(max_length=30)
    Valor = models.DecimalField(decimal_places=2,max_digits=1000)
    Ativo = models.BooleanField(default=True)
    categorias = models.ManyToManyField(Categoria, related_name='produtos')



# Create your models here.
