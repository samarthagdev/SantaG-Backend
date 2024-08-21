from django.shortcuts import render
from rest_framework import status, filters, generics
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import OfferPoster, OfferPoster1,OfferPoster2, OfferPoster3
from .serializers import OfferPosterSerilizer, OfferPosterSerilizer1, OfferPosterSerilizer2, OfferPosterSerilizer3

# Create your views here.
@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def offerposter_list(request, format=None):
    """
    List all cosmatic.
    """
    snippets = OfferPoster.objects.all()
    serializer = OfferPosterSerilizer(snippets, many=True)
    return Response(serializer.data)

@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def offerposter_list1(request, format=None):
    """
    List all cosmatic.
    """
    snippets = OfferPoster1.objects.all()
    serializer = OfferPosterSerilizer1(snippets, many=True)
    return Response(serializer.data)

@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def offerposter_list2(request, format=None):
    """
    List all cosmatic.
    """
    snippets = OfferPoster2.objects.all()
    serializer = OfferPosterSerilizer2(snippets, many=True)
    return Response(serializer.data)

@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def offerposter_list3(request, format=None):
    """
    List all cosmatic.
    """
    snippets = OfferPoster3.objects.all()
    serializer = OfferPosterSerilizer3(snippets, many=True)
    return Response(serializer.data)