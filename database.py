import sqlite3

conn = sqlite3.connect("db.sqlite") 
cursor = conn.cursor()

# query=("""CREATE TABLE answers
#                   (id INTEGER  PRIMARY KEY AUTOINCREMENT, 
#                   msg TEXT, 
#                   answ TEXT)""")



# query=("""INSERT INTO answers(msg, answ) VALUES
#     ("Какой сейчас час?", "Час убивать!!!"),
#     ("Я ухожу", "Беги, беги, далеко не убежишь."),
#     ("/help", "Я тебе не Сири, чтобы показывать что у меня внутри."),
#     ("Почему ты злой?", "Я не злой, это ты просто скоро будешь мёртвым")
#         """
# )

# query=("""INSERT INTO answers(msg, answ) VALUES
#     ("Волк?", "Нет, но порвать тебя могу, а ещё я могу: \n
#     Привет\n
#     Какой сейчас час?\n
#     Почему ты злой?\n
#     /help\n
#     /say текст\n
#     Я ухожу
#     ")
#         """
# )

# query=("""CREATE TABLE Groups
#                   (id INTEGER  PRIMARY KEY AUTOINCREMENT, 
#                   GroupName TEXT)""")

query=("""CREATE TABLE User
                    (id INTEGER  PRIMARY KEY, 
                    groupId TEXT,
                    FOREIGN KEY (groupId) REFERENCES Groups(id))""")

cursor.execute(query)
conn.commit()
conn.close()

