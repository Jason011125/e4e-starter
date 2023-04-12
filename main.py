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
    # check whether we have a session exist
    mycursor.execute("SELECT * FROM classes WHERE end_time IS NULL")
    for x in mycursor:
        if x:
            print("need to end session before inserting a new one")
            return
    if start_time:
        start_time_insert = datetime.strptime(start_time, "%m/%d/%Y %H:%M:%S")
        date = datetime.strftime(start_time_insert, "%m/%d %Y")
    else:
        date = datetime.strftime(datetime.today(), "%m/%d %Y")
        chopped_time = datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f')
        start_time_insert = chopped_time[:-7]

    sql = "INSERT INTO classes (start_time, date) VALUES(%s,%s)"
    val = (start_time_insert, date)
    mycursor.execute(sql, val)
    db.commit()


# since we only have 1 table, print_db will help us see all the elements inside our db.
def print_db():
    mycursor.execute("SELECT * FROM classes")
    for x in mycursor:
        print(x);


def delete_db():
    mycursor.execute("DELETE FROM classes")


# in this time stop function, we need to input our class, then find our entry with no end time. After that, we can then
# assign our stop time to it if provided, other wise assign current time to be end time. class must be assigned.
def time_stop():
    input_class = input("enter input class:\n")
    end_time = input("enter end time or none to end right now:\n")
    # to check whether our input is null, if so, print usage and return.
    if input_class:
        mycursor.execute("SELECT * FROM classes WHERE end_time IS NULL")
        start_time = mycursor.fetchone()[2]
        start_time_obj = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
        if start_time is None:
            print("we do not have a session started yet,return\n")
            return

        if end_time:
            end_time_obj = datetime.strptime(end_time, "%m/%d/%Y %H:%M:%S")
        else:
            end_time_obj = datetime.now()
        if (start_time_obj > end_time_obj):
            print("start time is later than end time, check your inputs")
            return
        sql = "UPDATE classes SET name = %s, end_time = %s WHERE end_time IS NULL"
        val = (input_class, end_time_obj)
        mycursor.execute(sql, val)
        db.commit()

#input has to be in the form mm/dd
def report():
    input_date = input("input desired date: ")
    if input_date:
        mycursor.execute("SELECT * FROM classes WHERE date='%s'" %input_date)
    else:
        input_date = datetime.strftime(datetime.today(), "%m/%d %Y")
        mycursor.execute("SELECT * FROM classes WHERE date='%s'" %input_date)
    for x in mycursor:
        start_time = datetime.strptime(x[2], '%Y-%m-%d %H:%M:%S')
        end_time = datetime.strptime(x[3], '%Y-%m-%d %H:%M:%S')
        class_name = x[1]
        elapsed_time = end_time - start_time
        print("Class name: ", class_name, "elapsed time: ", elapsed_time)

def entries():
    input_date = input("input desired date: ")
    if input_date:
        mycursor.execute("SELECT * FROM classes WHERE date='%s'" %input_date)
    else:
        input_date = datetime.strftime(datetime.today(), "%m/%d %Y")
        mycursor.execute("SELECT * FROM classes WHERE date='%s'" %input_date)
    print("Timeslots of the day: \n")
    i = 0
    for x in mycursor:
        start_time = datetime.strptime(x[2], '%Y-%m-%d %H:%M:%S')
        end_time = datetime.strptime(x[3], '%Y-%m-%d %H:%M:%S')
        print(i, ": start time: ", start_time, "end time: ", end_time,"\n")
        i=i+1

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
