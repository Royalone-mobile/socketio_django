from django.shortcuts import render
import json
# from .models import ChatSession, User, Chat

async_mode = None
import os
from django.http import HttpResponse
import socketio

basedir = os.path.dirname(os.path.realpath(__file__))
sio = socketio.Server(async_mode='eventlet')\

@sio.event
def connect(sid, environ):
	print('connect', sid)

@sio.event
def message(sid, data):
    print('message ', data)
    content = json.loads(data)
    command = content.get("command", None)
    room_id = content.get("room", None)
    room_name = 'room_{}'.format(room_id)
    
    if command == "join":
        sio.enter_room(sid, room_name)
    elif command == "leave":
        sio.leave_room(sid, room_name)
    elif command == "send":
        sio.emit('message', data, room=room_name, skip_sid=sid)
        # self.update_chat(room_id, content["username"], content["message"])
        # self.send_room(content["room"], content["message"], content["username"])
@sio.event
def disconnect(sid):
    print('disconnect ', sid)

# def update_chat(self, room_id, username, message):
#     sessions = ChatSession.objects.filter(id=room_id)
#     session: ChatSession = sessions.first()
#     users = User.objects.filter(username=username)
#     user = users.first()
#     Chat.objects.create(user=user,
#                     chatSession=session,
#                     content=message)

# @sio.on('connection-bind')
# def connection_bind(sid, data):
# 	pass
    
# @sio.on('disconnect')
# def test_disconnect(sid):
#     pass

# Create your views here.

# import eventlet
# import socketio

# sio = socketio.Server()
# app = socketio.WSGIApp(sio, static_files={
#     '/': {'content_type': 'text/html', 'filename': 'index.html'}
# })

# @sio.event
# def connect(sid, environ):
#     print('connect ', sid)

# @sio.event
# def my_message(sid, data):
#     print('message ', data)

# @sio.event
# def disconnect(sid):
#     print('disconnect ', sid)


# eventlet.wsgi.server(eventlet.listen(('', 5000)), app)

# https://python-socketio.readthedocs.io/en/latest/intro.html
# https://www.botreetechnologies.com/blog/django-websocket-with-socketio
# python manage.py runserver --nothreading --noreload