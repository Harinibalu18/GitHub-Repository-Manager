from repository import Repository
from commit import Commit
from branch import Branch
from collaborator import Collaborator


class GitHubManager:

    def __init__(self):
        self.repositories = []

    # -----------------------------
    # Find Repository
    # -----------------------------
    def find_repository(self):

        if len(self.repositories) == 0:
            print("\nNo repositories available.")
            return None

        name = input("Enter Repository Name: ")

        for repo in self.repositories:
            if repo.name.lower() == name.lower():
                return repo

        print("Repository Not Found!")
        return None

    # -----------------------------
    # Create Repository
    # -----------------------------
    def create_repository(self):

        name = input("Repository Name : ")
        owner = input("Owner Name      : ")

        repo = Repository(name, owner)

        self.repositories.append(repo)

        print("\nRepository Created Successfully!")

    # -----------------------------
    # View Repositories
    # -----------------------------
    def view_repositories(self):

        if len(self.repositories) == 0:
            print("\nNo Repositories Found!")
            return

        for repo in self.repositories:
            repo.display()

    # -----------------------------
    # Delete Repository
    # -----------------------------
    def delete_repository(self):

        repo = self.find_repository()

        if repo:
            self.repositories.remove(repo)
            print("Repository Deleted Successfully!")

    # -----------------------------
    # Add Commit
    # -----------------------------
    def add_commit(self):

        repo = self.find_repository()

        if repo:

            message = input("Commit Message : ")
            author = input("Author         : ")

            commit = Commit(message, author)

            repo.commits.append(commit)

            print("Commit Added Successfully!")

    # -----------------------------
    # View Commits
    # -----------------------------
    def view_commits(self):

        repo = self.find_repository()

        if repo:

            if len(repo.commits) == 0:
                print("No Commits Available!")
                return

            for commit in repo.commits:
                commit.display()

    # -----------------------------
    # Create Branch
    # -----------------------------
    def create_branch(self):

        repo = self.find_repository()

        if repo:

            branch_name = input("Branch Name : ")

            for branch in repo.branches:
                if isinstance(branch, Branch):
                    if branch.name == branch_name:
                        print("Branch Already Exists!")
                        return
                else:
                    if branch == branch_name:
                        print("Branch Already Exists!")
                        return

            repo.branches.append(Branch(branch_name))

            print("Branch Created Successfully!")

    # -----------------------------
    # View Branches
    # -----------------------------
    def view_branches(self):

        repo = self.find_repository()

        if repo:

            for branch in repo.branches:

                if isinstance(branch, Branch):
                    branch.display()

                else:
                    print("\nBranch :", branch)

    # -----------------------------
    # Add Collaborator
    # -----------------------------
    def add_collaborator(self):

        repo = self.find_repository()

        if repo:

            name = input("Name  : ")
            email = input("Email : ")
            role = input("Role (Owner/Developer/Maintainer/Viewer): ")

            collaborator = Collaborator(name, email, role)

            repo.collaborators.append(collaborator)

            print("Collaborator Added Successfully!")

    # -----------------------------
    # View Collaborators
    # -----------------------------
    def view_collaborators(self):

        repo = self.find_repository()

        if repo:

            if len(repo.collaborators) == 0:
                print("No Collaborators Found!")
                return

            for collaborator in repo.collaborators:
                collaborator.display()