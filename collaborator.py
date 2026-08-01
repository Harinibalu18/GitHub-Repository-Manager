from datetime import datetime


class Collaborator:

    def __init__(self, name, email, role):

        self.name = name
        self.email = email
        self.role = role
        self.join_date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    def display(self):

        print("\n----------------------------")
        print("Name      :", self.name)
        print("Email     :", self.email)
        print("Role      :", self.role)
        print("Joined On :", self.join_date)