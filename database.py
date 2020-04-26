import sqlite3

conn = sqlite3.connect("db.sqlite") 
cursor = conn.cursor()

# cursor.execute("""CREATE TABLE cars
#                   (id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, mark text, color text,
#                    number text)
#                """)

# cursor.execute("""INSERT INTO cars(mark, color, number) VALUES ('Renault', 'red', 'к912ом'),
#                 ('Renault', 'blue', 'а707ма'),
#                 ('Volkswagen', 'green', 'а666мо'),
#                 ('Volga', 'yellow', 'c999ом');

#                 """
#                )
query="""
        SELECT * FROM cars
        """
cursor.execute(query)
result=cursor.fetchall()
print(result)
conn.commit()
conn.close()