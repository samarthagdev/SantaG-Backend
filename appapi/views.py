from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import status, filters, generics
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from cosmatic.models import Cosmaticitems
from .serializers import CosmaticSerilizer

# Create your views here.

@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def cosmatic_list(request, format=None):
    """
    List all cosmatic.
    """
    snippets = Cosmaticitems.objects.all()

    serializer = CosmaticSerilizer(snippets, many=True)
    return Response(serializer.data)


@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def cosmatic_detail(request, cosToken):
    """
    Retrieve, update or delete a code snippet.
    """

    try:
        snippet = Cosmaticitems.objects.get(cosToken=cosToken)
    except Cosmaticitems.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':

        serializer = CosmaticSerilizer(snippet,)
        
        return Response(serializer.data)

class UserListView(generics.ListAPIView):
    search_fields = ['^cosBrand', 'cosName', 'cosBrand', '^specialuri', 'specialuri']
    filter_backends = (filters.SearchFilter,)
    queryset = Cosmaticitems.objects.all()
    serializer_class = CosmaticSerilizer
    # snippets = Cosmaticitems.objects.all()
    #
    # print(len(snippets))
    # print(snippets.get(cosToken='cos2').cosToken)
    def get_queryset(self):
        return Cosmaticitems.objects.filter()


