from datetime import datetime


class Branch:

    def __init__(self, name):

        self.name = name

        self.status = "Active"

        self.created_date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    def merge(self):

        self.status = "Merged"

    def display(self):

        print("\n----------------------------")
        print("Branch Name :", self.name)
        print("Status      :", self.status)
        print("Created On  :", self.created_date)