from rest_framework import status, filters, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from account.models import Account
from account.serializers import AccountSerilizer


# Create your views here.

@api_view(['POST'])
def UserCorrections(request):
    try:
        s = Account.objects.get(number=request.data.get('number'))
        content = {"username":s.userName}
        return Response(data= content)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def Setpass(request):
    if request.method == "POST":
        try:
            s = Account.objects.get(number=request.data.get('number'))
            s.userName = request.data.get('username')
            s.set_password(request.data.get('password'))
            s.save()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(status= status.HTTP_200_OK)