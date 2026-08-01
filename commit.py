from datetime import datetime


class Commit:

    commit_count = 1000

    def __init__(self, message, author):

        Commit.commit_count += 1

        self.commit_id = "C" + str(Commit.commit_count)

        self.message = message

        self.author = author

        self.date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    def display(self):

        print("\n------------------------------")
        print("Commit ID :", self.commit_id)
        print("Message   :", self.message)
        print("Author    :", self.author)
        print("Date      :", self.date)