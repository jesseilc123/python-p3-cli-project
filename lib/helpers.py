def main_menu():
    choice = 0

    print("***Enter the corresponding number***")
    print("1) Player menu")
    print("2) World menu")
    print("3) Server menu")
    print("4) Exit")

    while choice !=4:
        choice = int(input())
        if choice == 1:
            print("***Player Menu***")
            print("1) Lookup Player")
            print("2) Display all Players")
            print("3) Back to Main Menu")
        if choice == 2:
            print("***World Menu***")
            print("1) Lookup World")
            print("2) Display all Worlds")
            print("3) Back to Main Menu")
        if choice == 3:
            print("***Server Menu***")
            print("1) Lookup Server")
            print("2) Display all Servers")
            print("3) Back to Main Menu")
        if choice == 4:
            print("Quiting Program")
            print("Program Terminated")

def sub_menu():
    sub_choice = 0
    sub_choice = int(input())
    if sub_choice == 1:
        print("test for look up")
    if sub_choice == 2:
        print("test for display")
    if sub_choice == 3:
        print("test for back")
    
