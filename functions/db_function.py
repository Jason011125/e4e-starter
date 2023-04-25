import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="xuan2001",
    database="mydatabase"
)

mycursor = db.cursor()
def db_initialize():
  mycursor.execute("CREATE DATABASE mydatabase")
  mycursor.execute(
    "CREATE TABLE classes (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), start_time VARCHAR(255),end_time VARCHAR(255),date VARCHAR(100))")

# since we only have 1 table, print_db will help us see all the elements inside our db.
def print_db():
    mycursor.execute("SELECT * FROM classes")
    for x in mycursor:
        print(x);


def delete_db():
    mycursor.execute("DELETE FROM classes")
    db.commit()


