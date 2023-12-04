import json
from channels.consumer import AsyncConsumer
from django.contrib.auth import get_user_model
from channels.db import database_sync_to_async
from .models import Thread, ChatMessage, Status
from home.models import Available_Status
from notifications.signals import notify
from django.utils.html import strip_tags
import re
from django.template.defaultfilters import escape_filter, urlizetrunc, escapejs_filter, date, truncatechars


user = get_user_model()

class ActiveConsumer(AsyncConsumer):
  async def websocket_connect(self, event):
    if self.scope['user'].is_authenticated and self.scope['user'].is_active:
     print("connect", event)
     await self.channel_layer.group_add(
      f"chat_room_{self.scope['user'].id}",
      self.channel_name
      )
     await self.channel_layer.group_add(
      "status",
      self.channel_name
      )
     await self.send({
       'type': 'websocket.accept'
     })
     await available_status(self.scope["user"].id)
     nuser = self.scope["user"]
     response = {
        'type': "available",
        'status': "online",
        'user': self.scope["user"].id,
      }
     await self.channel_layer.group_send(
        "status",
        {
          "type": "chat_message",
          "text": json.dumps(response),
          "nuser": nuser,
      })

  async def websocket_receive(self, event):
    print("receive", event)

  async def websocket_disconnect(self, event):
    print("disconnect", event)
    await unavailable_status(self.scope["user"].id)
    nuser = self.scope["user"]

    response = {
      'type': "available",
      'status': "offline",
      'user': self.scope["user"].id,
    }
    await self.channel_layer.group_send(
      "status",
      {
        "type": "chat_message",
        "text": json.dumps(response),
        "nuser": nuser,
    })
   
  async def chat_message(self, event):
    print("chat_message", event)
    
    # notify.send(sender = event["nuser"], recipient=self.scope["user"], verb="You just have a new message")
    await self.send({
      'type': 'websocket.send',
      'text': event["text"]
    })

class ChatConsumer(AsyncConsumer):
   async def websocket_connect(self, event):
    if self.scope['user'].is_authenticated and self.scope['user'].is_active:
     print("connect", event)
     await self.channel_layer.group_add(
      f"chat_room_{self.scope['user'].id}",
      self.channel_name
      )
     await self.channel_layer.group_add(
      "status",
      self.channel_name
      )

     await self.send({
       'type': 'websocket.accept'
     })
     await online_status(self.scope["user"].id)
     nuser = self.scope["user"]
     response = {
        'type': "status",
        'status': "online",
        'user': self.scope["user"].id,
      }
     await self.channel_layer.group_send(
        "status",
        {
          "type": "chat_message",
          "text": json.dumps(response),
          # "nuser": nuser,
      })

   async def websocket_receive(self, event):
     print(f"message-{self.scope['user']}", event)
     receive_data = json.loads(event['text'])
     typers = receive_data.get('type')
     if typers == "read":
      thread = receive_data.get('thread')
      user = self.scope['user']
      thread_obj = await get_thread_obj(int(thread))
      other_user = await get_other_user_obj(thread_obj.id, user)
      print("other_user", other_user)
      await edit_chat_obj(thread_obj.id, other_user)


     if typers == "message":
      msg = receive_data.get('message')
      thread = receive_data.get('thread')
      other_user = receive_data.get('other_user')
      user = self.scope["user"]
      me_obj = self.scope["user"] 

      if not msg:
        return False
      if not thread:
        return False
      if not other_user:
        return False
      if not user:
        return False

      thread_obj = await get_thread_obj(thread)
      other_obj = await get_user_obj(other_user)

      chat_t = await create_message(me_obj, msg, thread_obj, other_obj)
      
      chat_ts = date(chat_t, "h:i A")

      msg = await validate_value(msg)
      # msg = strip_tags(msg)
      truncMsg = truncatechars(msg,25)

      response = {
        'type': "message",
        'thread': thread,
        'chat_t': chat_ts,
        'other_name': other_obj.username,
        'name': user.username,
        'name_id': user.id,
        'other_id': other_obj.id,
        'message': msg,
        'truncmsg': truncMsg,
        'user': user.id,
      }

      await self.channel_layer.group_send(
        f"chat_room_{other_obj.id}",
        {
          "type": "chat_message",
          "text": json.dumps(response),
      })

      await self.channel_layer.group_send(
        f"chat_room_{self.scope['user'].id}",
        {
          "type": "chat_message",
          "text": json.dumps(response),
      })
     
   async def websocket_disconnect(self, event):
     print('disconnect', event)
     await offline_status(self.scope["user"].id)
     nuser = self.scope["user"]

     response = {
        'type': "status",
        'status': "offline",
        'user': self.scope["user"].id,
      }
     await self.channel_layer.group_send(
        "status",
        {
          "type": "chat_message",
          "text": json.dumps(response),
          # "nuser": nuser,
      })
   
   async def chat_message(self, event):
    print("chat_message", event)
    
    # notify.send(sender = event["nuser"], recipient=self.scope["user"], verb="You just have a new message")
    await self.send({
      'type': 'websocket.send',
      'text': event["text"]
    })


@database_sync_to_async
def create_message(users, msg, thread, toUser):
  obj = ChatMessage.objects.create(thread_id=thread.id, user_id=users.id, message=msg, to=toUser)
  return obj.timestamp

@database_sync_to_async
def get_user_obj(users_id):
  use_obj = user.objects.get(id = users_id)
  if use_obj:
    return use_obj
  return None

@database_sync_to_async
def online_status(users_id):
  use_obj = Status.objects.filter(profile_id = users_id).first()
  if use_obj:
    use_obj.online = True
    use_obj.save()
  else:
    Status.objects.create(profile_id=users_id, online=True)

@database_sync_to_async
def available_status(users_id):
  use_obj = Available_Status.objects.filter(profile_id = users_id).first()
  if use_obj:
    use_obj.online = True
    use_obj.save()
  else:
    Available_Status.objects.create(profile_id=users_id, online=True)

@database_sync_to_async
def offline_status(users_id):
  use_obj = Status.objects.filter(profile_id = users_id).first()
  if use_obj:
    use_obj.online = False
    use_obj.save()
  else:
    Status.objects.create(profile_id=users_id, online=False)

@database_sync_to_async
def unavailable_status(users_id):
  use_obj = Available_Status.objects.filter(profile_id = users_id).first()
  if use_obj:
    use_obj.online = False
    use_obj.save()
  else:
    Available_Status.objects.create(profile_id=users_id, online=False)
  
@database_sync_to_async
def get_other_user_obj(thread_id, users):
  other_obj = Thread.objects.get(id = thread_id)
  if other_obj.seller == users:
    return other_obj.buyer
  else:
    return other_obj.seller

@database_sync_to_async
def get_thread_obj(thread_id):
  use_obj = Thread.objects.get(id=thread_id)
  if use_obj:
    return use_obj
  return None

@database_sync_to_async
def edit_chat_obj(thread_id, user):
  chat_obj = ChatMessage.objects.filter(thread_id=thread_id, user_id = user.id)
  for i in chat_obj:
    i.unread = False
    i.save()

async def validate_value(value):
  results = re.findall('<script[^\n]*', value)
  for i in results:
    value = value.replace(i, escape_filter(i))
  result = re.findall('src=[\'\"][a-zA-Z0-9-._]+.js[\"\']', value)
  for i in result:
    value = value.replace(i, '')
  script_rmv = value.replace("<script>", escape_filter("<script>")).replace("</script>", escape_filter("</script>"))
  return urlizetrunc(script_rmv, limit=14, autoescape=True)

