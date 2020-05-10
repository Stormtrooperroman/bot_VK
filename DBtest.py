import sqlite3

conn = sqlite3.connect("cars.sqlite") 
cursor = conn.cursor()

##user
##car
##inform

cursor.execute("PRAGMA foreign_keys = ON")
# query=("""CREATE TABLE inform
#                   (id INTEGER  PRIMARY KEY AUTOINCREMENT, 
#                   number INTEGER,
#                   color TEXT, 
#                   id_owner TEXT NOT NULL,
#                   id_model TEXT NOT NULL,
#                   FOREIGN KEY (id_owner) REFERENCES user(id),
#                   FOREIGN KEY (id_model) REFERENCES car(id))""")

# query=("""INSERT INTO user(owner, driver_card) VALUES
#         ("Вася", 123)
#         """
# )
query =""" SELECT * FROM inform """
cursor.execute(query)
answer = cursor.fetchall()
print(answer)

# query=("""INSERT INTO car(mark, model, prod_country) VALUES
#         ("Toyota", "Camry", "Japan")
#         """
# )

# query=("""INSERT INTO inform(number, color, id_owner, id_model) VALUES
#         (758, "red", 1, 1)
#         """
# )
# query=("""DROP TABLE inform
#         """)
#cursor.execute(query)
conn.commit()
conn.close()