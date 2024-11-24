import csv
import os

PATH = os.path.join(os.path.dirname(__file__), 'contacts.csv')


class Commands:

    def __init__(self, path: str = PATH):
        self.path = path

    def add(self, contact) -> None:
        infos = [
            contact.name, contact.last_name, contact.number, contact.email
        ]
        if not os.path.isfile(self.path):
            headers = ["name", "last name", "number", "email"]
            with open("contacts.csv", "w", newline="") as file:
                csv_header = csv.DictWriter(file, fieldnames=headers)
                csv_header.writeheader()
        with open("contacts.csv", "a", newline="") as file:
            csvfile_writer = csv.writer(file)
            csvfile_writer.writerow(infos)

    @staticmethod
    def display() -> None:
        with open("contacts.csv", "r", newline="") as file:
            file_reader = csv.DictReader(file)
            for row in file_reader:
                name, last_name, number, email = row["name"], row[
                    "last name"], row["number"], row["email"]
                print(
                    f"\n{name} {last_name}\nNumber: {number}\nEmail: {email}")

    @staticmethod
    def form() -> list[str]:
        name_ipt = input("Name:\n").capitalize()
        last_name_ipt = input("Last Name:\n").capitalize()
        number_ipt = input("Number:\n")
        email_ipt = input("Email:\n").lower()
        return [name_ipt, last_name_ipt, number_ipt, email_ipt]

    @staticmethod
    def search() -> str:
        contact_name_ipt = input(
            "\nEnter the name of the contact you are looking for:\n").lower()
        with open("contacts.csv", "r") as file:
            file_reader = csv.DictReader(file)
            for row in file_reader:
                if row["name"].lower() == contact_name_ipt:
                    return f"\nContact details for {contact_name_ipt.capitalize()}:\nLast Name: {row['last name']}\nNumber: {row['number']}\nEmail: {row['email']}"
        return "\nContact not found."
