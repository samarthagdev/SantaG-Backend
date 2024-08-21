from rest_framework import status, filters, generics
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Userdasboard
from .serializers import UserdasSerilizer

# Create your views here.

@api_view(['GET'])
def userdaspage(request, format=None):
    """
    List all page structuer.
    """
    snippets = Userdasboard.objects.all()
    serializer = UserdasSerilizer(snippets, many=True)
    return Response(serializer.data)

