from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Produto
from .serializers import ProdutoSerializer

def produtos(request):
    produtos = Produto.objects.all()
    return render(request,"produtos.html",{"produtos": produtos})

@api_view(['POST'])
def addprodutos(request):
    serializer = ProdutoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# Create your views here.
