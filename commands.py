import csv
import os
import time
import sys

# Folder path, contacts.csv is added to path to verify if it exist or not for the add() method.
PATH = os.path.join(os.path.dirname(__file__), 'contacts.csv')


class Commands:

    def __init__(self, path: str = PATH):
        self.path = path
    #TODO: If the file exists but there is no header, it needs to be added.
    def add(self, contact) -> None:
        infos = [
            contact.name, contact.last_name, contact.number, contact.email
        ]
        if not os.path.isfile(self.path):
            headers = ["name", "last name", "number", "email"]
            with open("contacts.csv", "w", newline="") as file:
                csv_header = csv.DictWriter(file, fieldnames=headers)
                csv_header.writeheader()
        # if the .csv file already exists, it will just open it and append the new infos for the contact.
        with open("contacts.csv", "a", newline="") as file:
            csvfile_writer = csv.writer(file)
            csvfile_writer.writerow(infos)
        print("Adding contact...")

    @staticmethod
    def display() -> None:
        try:  # Check if file exist when the user tries to access it.
            with open("contacts.csv", "r", newline="") as file:
                file_reader = csv.DictReader(file)
                for row in file_reader:
                    name, last_name, number, email = row["name"], row[
                        "last name"], row["number"], row["email"]
                    print(
                        f"\n{name} {last_name}\nNumber: {number}\nEmail: {email}"
                    )
                    time.sleep(0.4)
        except Exception:  #Exits the command with an informational message (Error: FileNotFoundError).
            print("Please add a contact to create a contact list.")

    @staticmethod
    def search() -> str:
        contact_name_ipt = input(
            "\nEnter the name of the contact you are looking for:\n").lower()
        with open("contacts.csv", "r") as file:
            file_reader = csv.DictReader(file)
            for row in file_reader:
                if row["name"].lower() == contact_name_ipt:
                    time.sleep(0.4)
                    return f"\nContact details for {contact_name_ipt.capitalize()}:\nLast Name: {row['last name']}\nNumber: {row['number']}\nEmail: {row['email']}"
        time.sleep(0.4)
        return "\nContact not found."

    #TODO: The list does not update, to be fixed tomorrow (in progress)
    def edit() -> str:
        contact_name = input("\nInsert contact's name: ").lower()
        with open("contacts.csv", "r") as file:
            file_reader = csv.DictReader(file)
            udpated_data = []
            fieldnames = file_reader.fieldnames # store the fieldnames for the header later
            for row in file_reader:
                if row["name"].lower() == contact_name:
                    user_ipt = input("\nWhat do you want to edit?\n1) Number\n2) Email\n")
                    if user_ipt == "1":
                        new_number = input("What will the new number be?\n")
                        row["number"] == new_number
                    elif user_ipt == "2":
                        new_email = input("What will the new email be?\n")
                        row["email"] == new_email
                    else:
                        return "Option not available.\n"
        with open("contacts.csv", "w") as new_modified_file:
            file_writer = csv.DictWriter(new_modified_file, fieldnames=fieldnames)
            file_writer.writeheader() # add the header again
            file_writer.writerows(rows) #add the now update rows 
        time.sleep(0.4)
        return f"\nNo contact found with the name {contact_name.capitalize()}."


    def remove():
        ...

    @staticmethod
    def exit():
        print("Exiting app.")
        sys.exit()

    # < Not a command to manage the contact list >
    @staticmethod
    def form() -> list[str]:
        name_ipt = input("Name:\n").capitalize()
        last_name_ipt = input("Last Name:\n").capitalize()
        number_ipt = input("Number:\n")
        email_ipt = input("Email:\n").lower()
        return [name_ipt, last_name_ipt, number_ipt, email_ipt]
