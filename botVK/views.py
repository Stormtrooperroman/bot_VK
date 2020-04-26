from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render
import json
import vk
import random

token=""
session=vk.Session(access_token=token)
vkAPI=vk.API(session)

## Подтверждение сервера
@csrf_exempt
def confirmation(request):
    return HttpResponse('29c59b15')

@csrf_exempt
def bot(request):
    body=json.loads(request.body)
    print(body)
    if body == { "type": "confirmation", "group_id": 194135917 }:
        return HttpResponse('29c59b15')
    if body["type"]=="message_new":
        userID=body["object"]["message"]["from_id"]
        tag_rep=(body["object"]["message"]["text"]).split(" ", maxsplit=1)
        if body ["object"]["message"]["text"]=="Привет":
            name_us = vkAPI.users.get(user_ids = userID, v=5.103)
            msg = "Привет "+ name_us[0]["first_name"] +", я Твой самый лучший друг, я сниму с тебя скальп 💀 💀 💀 :)"
            vkAPI.messages.send(user_id=userID, message=msg, random_id=random.randint(1, 99999999999999), v=5.103)
        elif body ["object"]["message"]["text"]=="Какой сейчас час?":
            msg = "Час убивать!!!"
            vkAPI.messages.send(user_id=userID, message=msg, random_id=random.randint(1, 99999999999999), v=5.103)
        elif body ["object"]["message"]["text"]=="Почему ты злой?":
            msg = "Я не злой, это ты просто скоро будешь мёртвым"
            vkAPI.messages.send(user_id=userID, message=msg, random_id=random.randint(1, 99999999999999), v=5.103)
        elif body ["object"]["message"]["text"]=="Я ухожу":
            msg = " Беги, беги, далеко не убежишь."
            vkAPI.messages.send(user_id=userID, message=msg, random_id=random.randint(1, 99999999999999), v=5.103)
        elif body ["object"]["message"]["text"]=="/help":
            msg = "Я тебе не Сири, чтобы показывать что у меня внутри."
            vkAPI.messages.send(user_id=userID, message=msg, random_id=random.randint(1, 99999999999999), v=5.103)
        if tag_rep[0]=="/say":
            msg=tag_rep[1]
            vkAPI.messages.send(user_id=userID, message=msg, random_id=random.randint(1, 99999999999999), v=5.103)
        #name_us = vkAPI.users.get(access_token = token, user_ids = userID, v=5.103)
        #name_us=json.loads(vkAPI.users.get(userID))
        #print(name_us[0]["first_name"])
    return HttpResponse("ok")        




