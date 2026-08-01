from branch import Branch

class Repository:

    def __init__(self, name, owner):

        self.name = name
        self.owner = owner

        self.commits = []

        self.branches = [Branch("main")]

        self.collaborators = []

    def display(self):

        print("\n========== Repository Details ==========")
        print("Repository :", self.name)
        print("Owner      :", self.owner)
        print("Branches   :", len(self.branches))
        print("Commits    :", len(self.commits))
        print("Collaborators :", len(self.collaborators))