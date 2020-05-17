import sqlite3

# conn = sqlite3.connect("db.sqlite") 
# cursor = conn.cursor()

# # query=("""CREATE TABLE answers
# #                   (id INTEGER  PRIMARY KEY AUTOINCREMENT, 
# #                   msg TEXT, 
# #                   answ TEXT)""")



# # query=("""INSERT INTO answers(msg, answ) VALUES
# #     ("Какой сейчас час?", "Час убивать!!!"),
# #     ("Я ухожу", "Беги, беги, далеко не убежишь."),
# #     ("/help", "Я тебе не Сири, чтобы показывать что у меня внутри."),
# #     ("Почему ты злой?", "Я не злой, это ты просто скоро будешь мёртвым")
# #         """
# # )

# # query=("""INSERT INTO answers(msg, answ) VALUES
# #     ("Волк?", "Нет, но порвать тебя могу, а ещё я могу: \n
# #     Привет\n
# #     Какой сейчас час?\n
# #     Почему ты злой?\n
# #     /help\n
# #     /say текст\n
# #     Я ухожу
# #     ")
# #         """
# # )

# # query=("""CREATE TABLE Groups
# #                   (id INTEGER  PRIMARY KEY AUTOINCREMENT, 
# #                   GroupName TEXT)""")

# # query=("""DROP TABLE User
# #             """)

# # query=("""CREATE TABLE User
# #                     (id INTEGER  PRIMARY KEY, 
# #                     groupId INTEGER,
# #                     FOREIGN KEY (groupId) REFERENCES Groups(id))""")
# query=("""INSERT INTO Groups(GroupName)VALUES
#             ("Boss"),
#             ("ProgramBoss"),
#             ("Person")
#             """)

# cursor.execute(query)
# conn.commit()
# conn.close()

def get(table_name, cols = "*"):
    db = sqlite3.connect('db.sqlite')
    cur = db.cursor()

    query = """
        SELECT {1} FROM {0}
        """.format(table_name,  cols if cols=="*" else "({0})".format(",".join(cols)))

    cur.execute(query)
    colNames = list(map(lambda x: x[0], cur.description))

    result = []

    for i in cur.fetchall():
        result.append(dict(zip(colNames, i)))
    db.close()

    return result

def insert(table_name, cols, data):
    db = sqlite3.connect('db.sqlite')
    cur = db.cursor()

    query = """
        INSERT INTO {0}({1})
        VALUES('{2}');
    """.format(table_name, ",".join(cols), "','".join(data))

    cur.execute(query)

    db.commit()
    db.close()

def getGroup(userID = None):
    db = sqlite3.connect('db.sqlite')
    cur = db.cursor()

    query = ""

    if userID == None:
        query = """
            SELECT * FROM Groups
            JOIN user
            ON Groups.id = user.groupId
        """
    else:
        query = """
            SELECT * FROM Groups
            INNER JOIN user
            ON Groups.id = user.groupId
            WHERE user.id == '{0}'
        """.format(userID) 

    cur.execute(query)
    colNames = list(map(lambda x: x[0], cur.description))

    result = []

    for i in cur.fetchall():
        result.append(dict(zip(colNames, i)))
    db.commit()
    db.close()

    return result

def deleteUser(userID = None):
    db = sqlite3.connect('db.sqlite')
    cur = db.cursor()

    if(getGroup(userID)) == []:
        db.commit()
        db.close()
        return "Ошибка, такого пользователя нет в Базе Данных"

    query = ""

    if userID == None:
        query = """
            DELETE FROM user
        """
    else:
        query = """
            DELETE FROM user
            WHERE user.id == '{0}'
        """.format(userID)
    
    cur.execute(query)
    db.commit()
    db.close()

    return "Вы были удалены из базы данных"

