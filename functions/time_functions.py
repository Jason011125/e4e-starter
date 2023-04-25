from .db_function import *
from datetime import datetime
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


# in this time stop function, we need to input our class, then find our entry with no end time. After that, we can then
# assign our stop time to it if provided, other wise assign current time to be end time. class must be assigned.
def time_stop():
    input_class = input("enter input class:\n")
    end_time = input("enter end time or none to end right now:\n")
    # to check whether our input is null, if so, print usage and return.
    if input_class:
        mycursor.execute("SELECT * FROM classes WHERE end_time IS NULL")
        res = mycursor.fetchone()
        if res is None:
            print("we do not have a session started yet,return\n")
            return
        start_time = res[2]
        start_time_obj = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')

        if end_time:
            end_time_obj = datetime.strptime(end_time, "%m/%d/%Y %H:%M:%S")
        else:
            end_time_obj = datetime.now()
        if start_time_obj > end_time_obj:
            print("start time is later than end time, check your inputs")
            return
        sql = "UPDATE classes SET name = %s, end_time = %s WHERE end_time IS NULL"
        val = (input_class, end_time_obj)
        mycursor.execute(sql, val)
        db.commit()
    else:
        print("wrong usage, class is required")
        return


# input has to be in the form mm/dd
def report():
    input_date = input("input desired date: ")
    if input_date:
        mycursor.execute("SELECT * FROM classes WHERE date='%s'" % input_date)
    else:
        input_date = datetime.strftime(datetime.today(), "%m/%d %Y")
        mycursor.execute("SELECT * FROM classes WHERE date='%s'" % input_date)
    for x in mycursor:
        start_time = datetime.strptime(x[2], '%Y-%m-%d %H:%M:%S')
        end_time = datetime.strptime(x[3], '%Y-%m-%d %H:%M:%S')
        class_name = x[1]
        elapsed_time = end_time - start_time
        print("Class name: ", class_name, "elapsed time: ", elapsed_time)


def entries():
    input_date = input("input desired date: ")
    if input_date:
        mycursor.execute("SELECT * FROM classes WHERE date='%s'" % input_date)
    else:
        input_date = datetime.strftime(datetime.today(), "%m/%d %Y")
        mycursor.execute("SELECT * FROM classes WHERE date='%s'" % input_date)
    print("Timeslots of the day: \n")
    i = 0
    for x in mycursor:
        start_time = datetime.strptime(x[2], '%Y-%m-%d %H:%M:%S')
        end_time = datetime.strptime(x[3], '%Y-%m-%d %H:%M:%S')
        print(i, ": start time: ", start_time, "end time: ", end_time, "\n")
        i = i + 1
