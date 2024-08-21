from django.shortcuts import render
from rest_framework import status, filters, generics
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Address
from .serializers import AddressSerilizer
# Create your views here.
@api_view(['POST'])

def AddressView(request):
    if request.method == 'POST':
        if Address.objects.filter(number=request.data.get("number")).exists():
            snippets = Address.objects.get(number=request.data.get("number"))
            serializer = AddressSerilizer(snippets)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(status=status.HTTP_400_BAD_REQUEST)