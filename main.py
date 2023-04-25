import functions

def main():
    option = input("press 1 for start, 2 for stop, 3 for report, 4 for entry, p for print, d for delete data,"
                   " q for quit\n")
    while option != "q":
        if option == "1":
            functions.time_start()
        elif option == "2":
            functions.time_stop()
        elif option == "3":
            functions.report()
        elif option == "4":
            functions.entries()
        elif option == "p":
            functions.print_db()
        elif option == "d":
            functions.delete_db()
        else:
            print("wrong usage")
        option = input("press 1 for start, 2 for stop, 3 for report, 4 for entry, p for print, q for quit\n")


main()
