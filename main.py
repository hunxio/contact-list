from contact import Contact
from commands import Commands
import time


def main():
    while True:
        user_option = input(
            "\nWhat do you wish to do?\n1)Add contact\n2)Access Contact List\n3)Search Contact\n4)Edit Contact\n5)Delete Contact\n6)Exit\nOption: "
        )
        if user_option == "1":
            #add()
            info = Commands().form()
            name, last_name, number, email = (
                info[0],
                info[1],
                info[2],
                info[3],
            )
            new_contact = Contact(name, last_name, number, email)
            Commands().add(new_contact)
        elif user_option == "2":
            #display()
            Commands().display()
        elif user_option == "3":
            #search()
            print(Commands().search())
        elif user_option == "4":
            # edit()
            ...
        elif user_option == "5":
            #remove()
            ...
        elif user_option == "6":
            #exit program
            ...
        else:
            print("Option not available.")
        time.sleep(1)


if __name__ == "__main__":
    main()
