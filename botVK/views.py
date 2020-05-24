from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render
import json
import vk
import random
import sqlite3
import database
##py manage.py runserver
##ssh -R 80:127.0.0.1:8000 botvkroman@ssh.localhost.run

token="67addbfd34b6c312db9998149a8a379cd0fbf4904f7725d6ce22c0f9f321029970d9bededa00a17b596ba"
session=vk.Session(access_token=token)
vkAPI=vk.API(session)

## Подтверждение сервера
@csrf_exempt
def confirmation(request):
    return HttpResponse('5ba3cbbe')

@csrf_exempt
def bot(request):
    body=json.loads(request.body)
    
    def SendAnswer(userID, msg, keyboard = ""):
        vkAPI.messages.send(user_id=userID, message=msg, keyboard=keyboard, random_id=random.randint(1, 99999999999999), v=5.103)

    print(body)
    if body == { "type": "confirmation", "group_id": 194135917 }:
        return HttpResponse('5ba3cbbe')
    if body["type"]=="message_new":
        msg=body ["object"]["message"]["text"]
        userID=body["object"]["message"]["from_id"]
        name_us = vkAPI.users.get(user_ids = userID, v=5.103)
        name_user=name_us[0]["first_name"]
        tag_rep=(msg).split(" ", maxsplit=1)
        answ=""
        gpid = -1
        gpname =""
        if "payload" in body["object"]["message"]:
            payload = body["object"]["message"]["payload"]
        def keyboardStart(request, userID):
	        answ = "Привет! Выбери свою группу пользователя!"
	        keyboard = json.dumps({
		    "one_time": True,

		    "buttons":[
                [{
				    "action": {
					    "type":"text",
					    "label":"Администратор",
					    "payload": """{"command":"admin"}"""
				    },
				        "color":"negative"
			        }
		        ],
                [{
				    "action": {
					    "type":"text",
					    "label":"Программист",
					    "payload": """{"command":"program"}"""
				    },
				        "color":"positive"
			        }
		        ],
                [{
				    "action": {
					    "type":"text",
					    "label":"Труп",
					    "payload": """{"command":"person"}"""
				    },
				        "color":"primary"
			        }
		        ]
                ]
	        })
	        SendAnswer(userID, answ, keyboard)
        if msg=="Привет":
            name_us = vkAPI.users.get(user_ids = userID, v=5.103)
            answ = "Привет "+ name_user +", я Твой самый лучший друг, я сниму с тебя скальп 💀 💀 💀 :)"
            SendAnswer(userID, answ)
        elif msg == "/whoAmI":
            answ = """Вы относитесь к группе {0}""".format(database.getGroup(str(userID))[0]["GroupName"])
            SendAnswer(userID, answ)
        elif msg=="/changeMeNow":
            database.deleteUser(userID)
            keyboardStart(request, userID)
            return 1

        elif tag_rep[0]=="/say":
            answ=tag_rep[1]
            SendAnswer(userID, answ)
        elif payload == """{"command":"start"}""":
            keyboardStart(request, userID)
        elif payload == """{"command":"admin"}""":
            gpid = str(1)
            gpname = "Администратор"
            database.insert("user", ["id, groupId"], [str(userID), gpid])
            answ= "Вы были добавлены в группу {0}".format(gpname)
            SendAnswer(userID, answ)
        elif payload == """{"command":"program"}""":
            gpid = str(2)
            gpname = "Программист"
            database.insert("user", ["id, groupId"], [str(userID), gpid])
            answ= "Вы были добавлены в группу {0}".format(gpname)
        elif payload == """{"command":"person"}""":
            gpid = str(3)
            gpname = "Труп"
            database.insert("user", ["id, groupId"], [str(userID), gpid])
            answ= "Вы были добавлены в группу {0}".format(gpname)
        else:
            conn = sqlite3.connect("db.sqlite") 
            cur = conn.cursor()
            query =""" SELECT * FROM answers """
            cur.execute(query)
            answer = cur.fetchall()
            conn.close()
            for i in range(len(answer)):
                if answer[i][1]==msg:
                    answ=answer[i][2]
                    SendAnswer(userID, answ)


        # elif body ["object"]["message"]["text"]=="Какой сейчас час?":
        #     msg = "Час убивать!!!"
        #     vkAPI.messages.send(user_id=userID, message=msg, random_id=random.randint(1, 99999999999999), v=5.103)
        # elif body ["object"]["message"]["text"]=="Почему ты злой?":
        #     msg = "Я не злой, это ты просто скоро будешь мёртвым"
        #     vkAPI.messages.send(user_id=userID, message=msg, random_id=random.randint(1, 99999999999999), v=5.103)
        # elif body ["object"]["message"]["text"]=="Я ухожу":
        #     msg = " Беги, беги, далеко не убежишь."
        #     vkAPI.messages.send(user_id=userID, message=msg, random_id=random.randint(1, 99999999999999), v=5.103)
        # elif body ["object"]["message"]["text"]=="/help":
        #     msg = "Я тебе не Сири, чтобы показывать что у меня внутри."
        #     vkAPI.messages.send(user_id=userID, message=msg, random_id=random.randint(1, 99999999999999), v=5.103)
        # if msg=="/help":
        #     conn = sqlite3.connect("db.sqlite") 
        #     cur = conn.cursor()
        #     query =""" SELECT * FROM answers """
        #     cur.execute(query)
        #     answer = cur.fetchall()
        #     conn.close()
        #     for i in range(len(answer)):
        #         if answer[i][1]==msg:
        #             answ=answer[i][2]
        #             SendAnswer(userID, answ)
        # elif msg=="Какой сейчас час?":
        #     conn = sqlite3.connect("db.sqlite") 
        #     cur = conn.cursor()
        #     query =""" SELECT * FROM answers """
        #     cur.execute(query)
        #     answer = cur.fetchall()
        #     conn.close()
        #     for i in range(len(answer)):
        #         if answer[i][1]==msg:
        #             answ=answer[i][2]
        #             SendAnswer(userID, answ)
        
        
        #name_us = vkAPI.users.get(access_token = token, user_ids = userID, v=5.103)
        #name_us=json.loads(vkAPI.users.get(userID))
        #print(name_us[0]["first_name"])
    
    
    return HttpResponse("ok")        

lg={
    "success": False,
    "groups":database.get("Groups", )

}

def SendAnswer(userID, msg, keyboard = ""):
        vkAPI.messages.send(user_id=userID, message=msg, keyboard=keyboard, random_id=random.randint(1, 99999999999999), v=5.103)

@csrf_exempt
def login(request):
    global lg
    print(lg)


    if request.method == "POST":
        print(request.POST)
        if request.POST.get("login") == "admin" and request.POST.get("password") == "0000":
            lg["success"] = True
        
        elif (request.POST.get("message") and request.POST.get("group")) != None:
            for user in database.getGroup(groupID = request.POST.get("group")):
                SendAnswer(user["id"], request.POST.get("message"))
        


    return render(request, "login.html", lg)


