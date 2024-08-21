from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from restro.models import RestroAccount, Categories, Items, PreviousStoreData
import string
import random
from .serializers import CategorySerilizer, ItemsSerilizer, BothItemNCategory, PreviousDataSerializer
from collections import namedtuple
import json

# Create your views here.
# creating socket




# Admin Login < used in admin/login.dart >

@api_view(['POST'])
def admin_login(request):
    if request.method == 'POST':
        tk = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=40))

        if RestroAccount.objects.filter(number=request.data.get('number'),
                                        password=request.data.get('password')).exists():
            ac = RestroAccount.objects.get(number=request.data.get('number'))
            if ac.is_admin:
                ac.tk = tk
                ac.firebasetk = request.data.get('firebasetoken')
                dic = {'tk':tk, 'unique_id':ac.unique_tag, 'userName': ac.userName}
                ac.save()
                return Response(status=status.HTTP_200_OK, data=dic)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


# Employee Login < used in employee/employee.dart >

@api_view(['POST'])
def employee_login(request):
    if request.method == 'POST':
        tk = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=40))

        if RestroAccount.objects.filter(number=request.data.get('number'),
                                        password=request.data.get('password')).exists():
            ac = RestroAccount.objects.get(number=request.data.get('number'))
            if ac.is_staff:
                ac.tk = tk
                ac.firebasetk = request.data.get('firebasetoken')
                dic = {'tk': tk, 'unique_id': ac.unique_tag, 'userName': ac.userName}
                ac.save()
                return Response(status=status.HTTP_200_OK, data=dic)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


# Checking Crediential used in < openingscreen.dart >

@api_view(['POST'])
def opening_login(request):
    if request.method == 'POST':
        tk = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=40))
        if RestroAccount.objects.filter(number=request.data.get('number'), tk=request.data.get('ky')).exists():
            ac = RestroAccount.objects.get(number=request.data.get('number'))
            dir = {}
            if ac.is_admin:
                dir['tk'] = tk
                dir['position'] = 'admin'
                ac.tk = tk
                ac.save()
                return Response(status=status.HTTP_200_OK, data=dir)

            if ac.is_staff:
                dir['tk'] = tk
                dir['position'] = 'employee'
                ac.tk = tk
                ac.save()
                return Response(status=status.HTTP_200_OK, data=dir)

            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


# adding employee <used in common/employee_add.dart>

@api_view(['POST'])
def adding_employee(request):
    if request.method == 'POST':
        tk = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=40))
        if len(request.data.get('number')) == 10:
            ac = RestroAccount(userName=request.data.get('name'), password=request.data.get('password'),
                               number=request.data.get('number'), unique_tag=request.data.get('uniqueid'),
                               tk=tk, is_staff=True, is_active=True)
            ac.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


# Adding Category for items

@api_view(['POST'])
def adding_category(request):
    if request.method == 'POST':
        try:
            if Categories.objects.filter(category=request.data.get('category')).exists():
                return Response(status=status.HTTP_205_RESET_CONTENT)
            category = Categories(category=request.data.get('category'))
            category.save()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def getting_previousData(request):
    if request.method == 'POST':
        if RestroAccount.objects.filter(tk=request.data.get('ky')).exists():
            previousData = PreviousStoreData.objects.all().order_by('id').reverse()
            a = []
            for x in previousData:
                x.table_data = eval(x.table_data)
                a.append({'uni_name': x.uni_name, 'table_no': x.table_no, 'table_data': x.table_data,
                          'order_taker': x.order_taker, 'time': x.time, 'net_amount': x.net_amount,
                          'position': x.position})
            return Response(data={'previous':a}, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
# Getting catergory used only in

@api_view(['GET'])
def getting_category(request):
    if request.method == 'GET':
        category = Categories.objects.all()
        serializer = CategorySerilizer(category, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def removing_category(request):
    if request.method == 'POST':
        if request.data.get('which') =='category':
            Categories.objects.filter(category=request.data.get('both')).delete()
            return Response(status=status.HTTP_200_OK, )
        elif request.data.get('which') == 'items':
            Items.objects.filter(items=request.data.get('both')).delete()
            return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


# Getting Categories and Items
@api_view(['GET'])
def getting_items(request):
    if request.method == 'GET':
        Timeline = namedtuple('Timeline', ('category', 'item'))
        s = Timeline(category=Categories.objects.all(), item=Items.objects.all())
        serializer = BothItemNCategory(s)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


# Adding items
@api_view(['POST'])
def adding_items(request):
    if request.method == 'POST':
        try:
            if Items.objects.filter(items=request.data.get('item')).exists():
                return Response(status=status.HTTP_205_RESET_CONTENT)
            item = Items(category_items=request.data.get('category'), price=request.data.get('price'),
                         items=request.data.get('item'))
            item.save()
            return Response(status=status.HTTP_200_OK, )
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

