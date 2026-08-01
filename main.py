from manager import GitHubManager


def main():

    manager = GitHubManager()

    while True:

        print("\n========== GitHub Repository Manager ==========")
        print("1. Create Repository")
        print("2. View Repositories")
        print("3. Add Commit")
        print("4. View Commits")
        print("5. Create Branch")
        print("6. View Branches")
        print("7. Add Collaborator")
        print("8. View Collaborators")
        print("9. Delete Repository")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            manager.create_repository()

        elif choice == "2":
            manager.view_repositories()

        elif choice == "3":
            manager.add_commit()

        elif choice == "4":
            manager.view_commits()

        elif choice == "5":
            manager.create_branch()

        elif choice == "6":
            manager.view_branches()

        elif choice == "7":
            manager.add_collaborator()

        elif choice == "8":
            manager.view_collaborators()

        elif choice == "9":
            manager.delete_repository()

        elif choice == "10":
            print("Thank you for using GitHub Repository Manager!")
            break

        else:
            print("Invalid Choice!")


if __name__ == "__main__":
    main()