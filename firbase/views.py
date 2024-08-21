from rest_framework import status, filters, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import devicetoken
# Create your views here.


@api_view(['POST'])
def firebasetoken(request):
    if request.method == 'POST':
        try:
            if devicetoken.objects.filter(number=request.data.get('number')).exists():
                token = devicetoken.objects.get(number=request.data.get('number'))
                if token.fcm_token != request.data.get('token'):
                    token.fcm_token = request.data.get('token')
                    token.save()
                    return Response(status=status.HTTP_200_OK)
                return Response(status=status.HTTP_205_RESET_CONTENT)
            else:
                firebase = devicetoken(number= request.data.get('number'), fcm_token= request.data.get('token'))
                firebase.save()
                return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

