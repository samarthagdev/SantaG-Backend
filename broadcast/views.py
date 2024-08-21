import json
import http.client
import random
import datetime
from django.conf import settings
from django.http import HttpResponse
from twilio.rest import Client
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from bag.models import FullOrder
from account.models import Account
from broadcast.models import Otpveification,Otpveification1, Version
from bag.serializers import FullOrderSerilizer
from broadcast.serializers import OtpSerilizer,OtpSerilizer1, UserRegistration

lis = []
for x in range(1, 10):
    for y in range(1, 10):
        for a in range(1, 10):
            for b in range(1, 10):
                lis1 = str(x) + str(y) + str(a) + str(b)
                if len(lis1) == 4:
                    lis.append(int(lis1))


@api_view(['POST'])
def otp_verification(request):

    if request.method == 'POST':
        try:
            s = Account.objects.get(number=request.data.get("number"))
            return Response(status=status.HTTP_400_BAD_REQUEST, data="This Number is Already Registered")
        except:

            if request.data.get("otp")!='1' or request.data.get("number_trial")!=0:
                return Response(status= status.HTTP_400_BAD_REQUEST, data='Restart the APP')
            otp = random.choice(lis)


            serializer = OtpSerilizer(data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save(otp = otp)
                number = request.data.get('number')


                if len(number) != 10:
                    if len(number) > 10 and not (number[0:3] == '+91' or number[0:2]=='91'):
                        return Response(status=status.HTTP_400_BAD_REQUEST,data="You Entered Wrong Digits of Mobile Number")
                    elif len(number) < 10:
                        return Response(status=status.HTTP_400_BAD_REQUEST,data="You Entered Wrong Digits of Mobile Number")
                try:
                    int(number)
                except:
                    return Response(status=status.HTTP_400_BAD_REQUEST,data="You Entered Wrong Digits of Mobile Number")

                if len(number) == 10:
                    if number[0:3] == '+91':
                        return Response(status=status.HTTP_400_BAD_REQUEST,data="You Entered Wrong Digits of Mobile Number")
                    number = '+91' + number
                    serializer.save(number=number, otp= otp)
                try:

                    message_to_broadcast = (
                        "Welcome to Agrawal Store. Here is your OTP for registration {otp}. please do not share your OTP with anyone".format(
                            otp=otp))
                    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
                    client.messages.create(to=number,
                                           from_=settings.TWILIO_NUMBER,
                                           body=message_to_broadcast)
                    return Response(status = status.HTTP_200_OK)
                except:
                    return Response(status=status.HTTP_400_BAD_REQUEST,data="Only local India mobile number is excepted")

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    else:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)





@api_view(['POST'])
def otp_checking(request):
    if request.method == 'POST':

        try:
            s = Account.objects.get(number=request.data.get("number"))
            return Response(status=status.HTTP_208_ALREADY_REPORTED)
        except:
            number = request.data.get("number")
            number = '+91' + number

            try:
                snippets = Otpveification.objects.filter(number=number).last()
            except Otpveification.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            if snippets.number_trial<4:


                if request.data.get("otp") == snippets.otp:
                    serializer = UserRegistration(data= request.data)

                    if serializer.is_valid(raise_exception=True):
                        account = serializer.save()
                        token = Token.objects.get(user= account).key

                        return Response(status=status.HTTP_200_OK, data=token)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                else:
                    number_trial = snippets.number_trial + 1
                    snippets.number_trial = number_trial
                    snippets.save()
                    return Response(status=status.HTTP_400_BAD_REQUEST, data = "Please write correct OTP.Number of trial left {s}".format(s =5-snippets.number_trial))
            else:
                return Response(status= status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)







@api_view(['POST'])
def otp_verification1(request):

    if request.method == 'POST':
        try:
            s = Account.objects.get(number=request.data.get("number"))
            if request.data.get("otp")!='1' or request.data.get("number_trial")!=0:
                return Response(status= status.HTTP_400_BAD_REQUEST, data='Restart the APP')
            otp = random.choice(lis)


            serializer = OtpSerilizer1(data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save(otp = otp)
                number = request.data.get('number')


                if len(number) != 10:
                    if len(number) > 10 and not (number[0:3] == '+91' or number[0:2]=='91'):
                        return Response(status=status.HTTP_400_BAD_REQUEST,data="You Entered Wrong Digits of Mobile Number")
                    elif len(number) < 10:
                        return Response(status=status.HTTP_400_BAD_REQUEST,data="You Entered Wrong Digits of Mobile Number")
                try:
                    int(number)
                except:
                    return Response(status=status.HTTP_400_BAD_REQUEST,data="You Entered Wrong Digits of Mobile Number")

                if len(number) == 10:
                    if number[0:3] == '+91':
                        return Response(status=status.HTTP_400_BAD_REQUEST,data="You Entered Wrong Digits of Mobile Number")
                    number = '+91' + number

                    serializer.save(number=number, otp= otp)
                try:

                    conn = http.client.HTTPConnection("2factor.in")

                    payload = ""

                    headers = {'content-type': "application/x-www-form-urlencoded"}

                    factor = "/API/V1/da764a2a-a1a6-11eb-80ea-0200cd936042/SMS/{number}/{otp}".format(number=number, otp=otp)
                    conn.request("GET", factor, payload,
                                 headers)

                    res = conn.getresponse()

                    return Response(status=status.HTTP_200_OK)



                    # message_to_broadcast = (
                    #     "Welcome to Agrawal Store. Here is your OTP for registration {otp}. please do not share your OTP with anyone".format(
                    #         otp=otp))
                    # client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
                    # client.messages.create(to=number,
                    #                         from_=settings.TWILIO_NUMBER,
                    #                         body=message_to_broadcast)

                except:
                    return Response(status=status.HTTP_400_BAD_REQUEST,data="Only local India mobile number is excepted")

            #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data= 'You do not have account with us')

    else:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)





@api_view(['POST'])
def otp_checking1(request):
    if request.method == 'POST':

        try:
            s = Account.objects.get(number=request.data.get("username"))
            number = request.data.get("username")
            number = '+91' + number

            try:
                snippets = Otpveification1.objects.filter(number=number).last()
            except Otpveification1.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            if snippets.number_trial < 4:
                if request.data.get("otp") == snippets.otp:
                    token = Token.objects.get(user=s).key
                    return Response(status=status.HTTP_200_OK, data=token)


                else:
                    number_trial = snippets.number_trial + 1
                    snippets.number_trial = number_trial
                    snippets.save()
                    return Response(status=status.HTTP_400_BAD_REQUEST,
                                    data="Please write correct OTP.Number of trial left {s}".format(
                                        s= 5 - snippets.number_trial))
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data='You do not have account')
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def landingpage(request):
    if request.method == 'POST':

        try:
            version_no = request.data.get('version')
            version_no1 = int(version_no.replace('.', ''))

            min_version = Version.objects.all().last()
            if version_no1 >= int(min_version.version):
                s = Account.objects.get(number=request.data.get("username"))
                token = Token.objects.get(user=s).key
                if request.data.get("token") == token:
                    return Response(status=status.HTTP_200_OK)
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(status=status.HTTP_205_RESET_CONTENT)

        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def sellerchecker(request):
    if request.method == 'POST':

        try:

            s = Account.objects.get(number=request.data.get("username"))

            token = Token.objects.get(user=s).key

            if request.data.get("token") == token:
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)

        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def santaorder(request):
    if request.method == 'POST':

        try:
            s = Account.objects.get(number=request.data.get("username"))
            token = Token.objects.get(user=s).key
            print(request.data.get("ui"))
            if request.data.get("ui") == token:
                if s.is_superuser or s.is_staff:
                    order = FullOrder.objects.all()

                    serializer = FullOrderSerilizer(order, many=True)
                    
                    return Response(status=status.HTTP_200_OK, data= serializer.data)
                else:
                    Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)

        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response(status=status.HTTP_404_NOT_FOUND)