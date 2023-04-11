from datetime import datetime
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="xuan2001",
    database="mydatabase"
)
mycursor = db.cursor()

# mycursor.execute("CREATE DATABASE mydatabase")
# mycursor.execute("CREATE TABLE classes (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), start_time VARCHAR(255),end_time VARCHAR(255),date VARCHAR(100))")

# structure of each element in our db: Class, Date, start time, end time.
# currently, input has to be in the format: mm/dd/yyyy h:m:second format
def time_start():
    start_time = input("input start time:")
    if start_time:
        mycursor.execute("SELECT * FROM classes WHERE end_time IS NULL")
        for x in mycursor:
            if x:
                print("need to end session before inserting a new one")
                return
        #need to check whether we have a session not ended yet, if so return, otherwise write to db.
        start_time_str = datetime.strptime(start_time, "%m/%d/%Y %H:%M:%S")
        print("Start time:", start_time_str)
        date = datetime.strftime(start_time_str, "%m/%d")
        sql = "INSERT INTO classes (start_time, date) VALUES(%s,%s)"
        val = (start_time_str, date)
        mycursor.execute(sql,val)
        db.commit()

    else:
        mycursor.execute("SELECT * FROM classes WHERE end_time IS NULL")
        for x in mycursor:
            if x:
                print("need to end session before inserting a new one")
                return

        print("Start time:", datetime.today())
        date = datetime.strftime(datetime.today(), "%m/%d")
        sql = "INSERT INTO classes (start_time, date) VALUES(%s,%s)"
        val = (datetime.today(), date)
        mycursor.execute(sql,val)
        db.commit()



#since we only have 1 table, print_db will help us see all the elements inside our db.
def print_db():
    mycursor.execute("SELECT * FROM classes")
    for x in mycursor:
        print(x);

def delete_db():
    mycursor.execute("DELETE FROM classes")
#in this time stop function, we need to input our class, then find our entry with no end time. After that, we can then
#assign our stop time to it if provided, other wise assign current time to be end time. class must be assigned. 
def time_stop(input_class, stop_time=None):
    print("lol")


def report():
    date = input("input desired  date: ")
    if date:
        print("info for input date")
    else:
        print("info for today")


def entries(date):
    print("lol")







def main():
    option = input("press 1 for start, 2 for stop, 3 for report, 4 for entry, p for print, q for quit\n")
    while option != "q":
        if option == "1":
            time_start()
        elif option == "2":
            time_stop()
        elif option == "3":
            report()
        elif option == "4":
            entries()
        elif option == "p":
            print_db()
        elif option == "d":
            delete_db()
        else:
            print("wrong usage")
        option = input("press 1 for start, 2 for stop, 3 for report, 4 for entry, p for print, q for quit\n")


main()
