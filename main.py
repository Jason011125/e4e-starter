from datetime import datetime
import json

#structure of each element in our db: Class, Date, start time, end time.







# currently, input has to be in the format: dd/mm/yyyy h:m:second format
def time_start():
    start_time = input("input start time:")
    if start_time:
        start_time_tuple = datetime.strptime(start_time, "%d/%m/%Y %H:%M:%S")
        # write to json db
        print("Start time:", start_time_tuple)
    else:
        print("Start time:", datetime.today())


def time_stop(inputclass, input_date_time):
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
    option = input("press 1 for start, 2 for stop, 3 for report, 4 for entry\n")
    if option == "1":
        time_start()
    elif option == "2":
        time_stop()
    elif option == "3":
        report()
    elif option == "4":
        entries()
    else:
        print("wrong usage")


main()
