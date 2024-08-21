from channels.db import database_sync_to_async
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Store, PreviousStoreData, RestroAccount
from datetime import datetime
import firebase_admin
from firebase_admin import credentials, messaging

dicdiffrentrestro = {}
cred = credentials.Certificate("C:/Users/91928/OneDrive/Desktop/Assignment/serviceAccountKey.json")
default_app = firebase_admin.initialize_app(cred)
registration_tokens = []

def fire(x,y, z, a, position,room):
    registration_tokens = list(dicdiffrentrestro[room]['admin'].values())
    message = messaging.MulticastMessage(
        android=messaging.AndroidConfig(
            notification=messaging.AndroidNotification(
            title='Bills is been {POSITION}'.format(POSITION=position),
            body='{tableno} {time} {employee} {amt} '.format(tableno=x, time=y, employee=z, amt=a,),
            priority='high',
            default_sound=True,
            )
        ),
        tokens=registration_tokens,
    )
    return message
def fire1(x, y, z , a,room):
    registration_tokens = list(dicdiffrentrestro[room]['admin'].values())
    message = messaging.MulticastMessage(
        android=messaging.AndroidConfig(
            notification=messaging.AndroidNotification(
                title='One item is cancelled',
                body='{tableno} {time} {employee} {itemname} '.format(tableno=x, time=y, employee=z, itemname=a),
                priority='high',
                default_sound=True,
            )
        ),
        tokens=registration_tokens,
    )
    return message


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        t = self.scope['headers']
        # number = ''
        for x in t:
            if b'number' in x:
                self.number = x[1].decode('UTF-8')
            if b'restroid' in x:
                self.room_name = x[1].decode('UTF-8')
                break
        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        message = await self.get_restromsg(s=self.room_name,)
        await self.accept()
        if len(message) != 0:
            await self.send(text_data=json.dumps({
                'message': message,
                'opened': True,
            }))



    @database_sync_to_async
    def get_restromsg(self, s,):
        d = Store.objects.filter(uni_name=self.room_group_name,).order_by('id')
        lis1 = []
        for x1 in d:
            lis1.append(x1.table_no)
        lis2 = []
        for x2 in list(set(lis1)):
            d1 = Store.objects.filter(uni_name=self.room_group_name, table_no=x2).order_by('id')
            lis2.append([eval(x.msg) for x in d1])
        lis = []
        for x in d:
            dis = eval(x.msg)
            lis.append(dis)
        a = RestroAccount.objects.get(unique_tag=s, number=self.number)
        if s in dicdiffrentrestro:
            if a.is_admin:
                if a.firebasetk != 0:
                    dicdiffrentrestro[s]['admin'][self.number] = a.firebasetk
            else:
                if a.firebasetk != 0:
                    dicdiffrentrestro[s]['employee'][self.number] = a.firebasetk
        else:
            dicdiffrentrestro[s] = {'admin': {}, 'employee': {}}
            if a.is_admin:
                if a.firebasetk != 0:
                    dicdiffrentrestro[s]['admin'][self.number] = a.firebasetk
            else:
                if a.firebasetk != 0:
                    dicdiffrentrestro[s]['employee'][self.number] = a.firebasetk
        return {'lis': lis, 'lis1': lis2}

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        # if message != 'close':
            # Send message to room group
        await self.adding(message)
        await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message,
                }
            )
        # else:
        #     self.close()

    async def chat_message(self, event):
        message = event['message']
        # Send message to WebSocket
        # print(type(message))
        # d= Question.objects.filter(restraunt_name=self.room_group_name)
        await self.send(text_data=json.dumps({
            'message': message,
            'opened': False,
        }))

    @database_sync_to_async
    def adding(self, mes):
        # type of mes is dict.
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        if 'position' in mes and mes['position'] == 'kitchen':
            s = Store.objects.filter(uni_name=self.room_group_name,).order_by('id')[mes['index']]
            if mes['process'] == 'In Process':
                _dic = eval(s.msg)
                _dic['process'] = 'Taken'
                s.msg = str(_dic)
                s.save()
            elif mes['process'] == 'Taken':
                _dic = eval(s.msg)
                _dic['process'] = 'Delivered'
                s.msg = str(_dic)
                s.save()
        elif'position' in mes and mes['position'] == 'cancelitem':
            a = Store.objects.filter(uni_name=self.room_group_name, table_no=mes['table_no']).order_by('id')
            lis = []
            lis1 = []
            i = 0
            s = 0
            for x in a:
                _dic1 = eval(x.msg)
                lis1.append(_dic1)
                lis.append([*range(s, s + len(_dic1['item_list']))])
                s += len(_dic1['item_list'])
            for x in lis:
                if mes['index'] in x:
                    index = lis[i].index(mes['index'])
                    del lis1[i]['item_list'][index]
                    break
                i += 1
            if len(lis1[i]['item_list']) == 0:
                a[i].delete()
            else:
                a[i].msg = str(lis1[i])
                a[i].save()
            message = fire1(x=mes['table_no'], y=dt_string, z=mes['username'], a=mes['itemname'], room=self.room_name)
            response = messaging.send_multicast(message)
        elif 'position' in mes and (mes['position'] == 'deletetable' or mes['position'] == 'finalize'):
            a = Store.objects.filter(uni_name=self.room_group_name, table_no=mes['table_no']).order_by('id')
            data = PreviousStoreData(uni_name=mes['unique'], table_no=mes['table_no'], table_data=mes['billdata'],
                                     net_amount=mes['netamount'], position=mes['position'], order_taker=mes['userName'],
                                     time=dt_string)
            message = fire(x=mes['table_no'], y=dt_string, z=mes['userName'], a=mes['netamount'], position=mes['position'], room=self.room_name)
            response = messaging.send_multicast(message)
            data.save()
            a.delete()
        else:
            a = Store(uni_name=self.room_group_name, msg=mes, table_no=mes['table_no'])
            a.save()

