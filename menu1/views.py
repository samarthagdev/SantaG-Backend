from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import status, filters, generics
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import MenuCard
from .serializers import MenuSerilizer

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def Menu_details(request):
    if request.method == 'GET':
        snippets = MenuCard.objects.all()
        serializer = MenuSerilizer(snippets, many=True)
        print(serializer.data)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)