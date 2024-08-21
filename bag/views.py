from firbase.models import devicetoken
from django.shortcuts import render
from rest_framework import status, filters, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from cosmatic.models import Cosmaticitems
from appapi.serializers import CosmaticSerilizer
from .models import BagAdding,Bagitems, AddToCart,FullOrder
import json
import requests
from address.models import Address
from .serializers import BagAddingSerilizer, BagitemSerilizer, AddtoCartSerilizer
# Create your views here.
serverToken = 'AAAAhT9ozkk:APA91bET3sh-3LwuAJ0m-CsDy3LiyGSCfV5sp_BXP4dagXNBgNMPTIGdlwUrtZeYhh0j5Zam1yPwghD9Lpbpx2JbO9qeDafUyikFctD0YDK3GSojOUD99Ps37sVLTl6-IFb14dx1ddSc'
deviceToken = 'dfFRje1VQXmpJOs2QsYtp3:APA91bFCx89Z4mJ1pKlRys4-YT50igcXrVHd9nsah3SUwNkaFfVGZ_p5QsxZY5zf5ti0BLRQ6eAdORYZiUJIZ_hleOjDXSMvpZXJLN4geM61bfD3VB2pOvwFyXYGycSuuf83CW4xfPZ0'

headers = {
        'Content-Type': 'application/json',
        'Authorization': 'key=' + serverToken,
      }

body = {
          'notification': {'title': 'SantaG',
                            'body': 'New Order'
                            },
          'to':
              deviceToken,
          'priority': 'high',

        }


@api_view(['POST'])
def BagView(request):
    if request.method == 'POST':
        if BagAdding.objects.filter(number=request.data.get("number"),cosToken=request.data.get("cosToken")).exists():

            BagAdding.objects.filter(number=request.data.get("number"),cosToken=request.data.get("cosToken")).update(cosQuantity=request.data.get("cosQuantity"))

            return Response(status=status.HTTP_200_OK)
        else:
            serializer = BagAddingSerilizer(data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(status= status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def ItemsView(request):
    if request.method == 'POST':
        try:
            snippets = BagAdding.objects.filter(number = request.data.get("number"))
            for x in snippets:
                snippets1 = Cosmaticitems.objects.get( cosToken= x.cosToken)
                if not Bagitems.objects.filter(number = request.data.get("number"), cosToken=x.cosToken).exists():
                    snippets2 = Bagitems(cosBrand=snippets1.cosBrand,cosName=snippets1.cosName,cosPrice=snippets1.cosPrice,cosDis=snippets1.cosDis,cosQuantity=snippets1.cosQuantity,cosToken=snippets1.cosToken,cosImage1=snippets1.cosImage1,measure=snippets1.measure,number = x.number, Quantityorder = x.cosQuantity)
                    snippets2.save()
                elif x.cosQuantity != None:
                    Bagitems.objects.filter(number=request.data.get("number"), cosToken= x.cosToken).update(Quantityorder = x.cosQuantity)
            snippets3 = Bagitems.objects.filter(number = request.data.get("number"))
            serializer = BagitemSerilizer(snippets3, many=True)
            return Response(status=status.HTTP_200_OK,data=serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def RemoveItemsView(request,):
    try:
        if request.method == 'POST':
            BagAdding.objects.filter(number=request.data.get('number'), cosToken=request.data.get('cosToken')).delete()
            Bagitems.objects.filter(number=request.data.get('number'), cosToken=request.data.get('cosToken')).delete()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    except Bagitems.DoesNotExist and BagAdding.DoesNotExist:
        return Response(status= status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def CartView(request):
    if request.method == 'POST':
        try:
            snippet1 = Address.objects.get(number=request.data.get('number'))
            if request.data.get('address') != snippet1.address:
                snippet1.address = request.data.get('address')
                snippet1.save()
        except:
            snippet1 = Address(address=request.data.get('address'), number=request.data.get('number'))
            snippet1.save()

        lis1 = []
        for x in request.data.get('items'):
            if Bagitems.objects.filter(number=request.data.get('number'), cosToken=x['cosToken']).exists():
                BagAdding.objects.get(number=request.data.get('number'), cosToken=x["cosToken"]).delete()
                Bagitems.objects.get(number=request.data.get('number'), cosToken=x['cosToken']).delete()

            s= x['cosImage1'][6::]
            snippets = AddToCart(cosName=x['cosName'], cosBrand=x['cosBrand'], cosQuantity=x['cosQuantity'],
                                 cosPrice=x['cosPrice'],cosDis=x['cosDis'],cosImage1=s,
                                 cosToken=x['cosToken'],measure=x['measure'],Quantityorder=x['Quantityorder'],
                                 number=x['number'],address=request.data.get('address'),)

            fullorder = 'Product Name: '+x['cosName']+' Brand: '+x['cosBrand']+' Quantity: '+str(x['Quantityorder'])+' Price: '+ str(x['cosPrice'])+' Dis: '+str(x['cosDis'])
            lis1.append(fullorder)

            snippets.save()
        str2 = 'Number: '+ request.data.get('number')+' Address: '+ request.data.get('address')+' Additional: '+request.data.get('additional')
        lis1.append(str2)
        s1 = """{}""".format("\n\n".join(i for i in lis1[0::]))
        str3 = FullOrder(fullorder=s1)
        str3.save()
        fcmresponse = requests.post("https://fcm.googleapis.com/fcm/send", headers=headers, data=json.dumps(body))
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def MyOrder(request):
    if request.method == "POST":
        try:
            snippets= AddToCart.objects.filter(number=request.data.get("number"))
            serializer = AddtoCartSerilizer(snippets, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status= status.HTTP_404_NOT_FOUND)
    return Response(status= status.HTTP_400_BAD_REQUEST)