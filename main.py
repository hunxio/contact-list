from contact import Contact
from commands import Commands


def main():
    user_option = input("Welcome User\nWhat do you wish to do?\n1)Add contact  2)Access Contact List\n")
    if user_option == "1":
        info = Commands().form()
        name, last_name, number, email = info[0], info[1], info[2], info[3],
        new_contact = Contact(name, last_name, number, email)
        Commands().add(new_contact)
    elif user_option == "2":
        Commands().display()
    else:
        print("Option not available, exiting application.")


if __name__ == "__main__":
    main()
