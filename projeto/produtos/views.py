from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Produto
from .serializers import *

def produtos(request):
    produtos = Produto.objects.prefetch_related('categorias').all()
    return render(request,"produtos.html",{"produtos": produtos})

@api_view(['POST'])
def addprodutos(request):
    serializer = ProdutoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def addCategorias(request):
    serializer = CategoriaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# Create your views here.
