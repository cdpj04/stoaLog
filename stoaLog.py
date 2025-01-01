import json
import sys
from datetime import datetime

journal = {}
# journal = {"title": {"entry": "date-time"}}

def main():
    first_run = True
    if first_run:
        print("\nWelcome to stoaLog :)")
        first_run = False
    while True:
        print("\n1. Add Entry")
        print("2. Delete Entry")
        print("3. View Entry")
        print("4. Search Entry")
        print("5. Save Journal")
        print("0. Exit")

        user_choice = input("Please choose an option: ")
        if user_choice == "1":
            add_entry()
        elif user_choice == "2":
            delete_entry()
        elif user_choice == "3":
            view_entry()
        elif user_choice == "4":
            search_journal()
        elif user_choice == "5":
            print("\nSaving journal...")
            save_journal()
        elif user_choice == "0":
            print("\nSaving journal...")
            save_journal()
            print("\nThank you for using stoaLog!")
            sys.exit(0)
        else:
            print("\nInvalid choice. Please try again.")

def add_entry():
    date = datetime.now().strftime("%Y-%m-%d")
    time = datetime.now().strftime("%H:%M")
    date_time = f"{date}, {time}"
    title = input("\nEntry title: ").strip().title()
    entry = input("Entry: ").strip()

    journal[title] = {"entry": entry, "date and time": date_time}
    print(f"\n{title} has been added to journal")

def delete_entry():
    if journal:
        print("\nJournal entries:")
        for i, title in enumerate(journal, 1):
            print(f"{i}. {title}")

        while True:
            user_choice = input("\nWhich entry would you like to delete? ").strip().title()
            if user_choice in journal:
                del journal[user_choice]
                save_journal()
                print(f"{user_choice} has been deleted from the journal and changes have been saved.")
                break
            else:
                print("\nInvalid choice. Please try again.")
    else:
        print("\nNo entries to delete") 

def view_entry():
    pass

def search_journal():
    pass

def save_journal():
    pass


if __name__ == "__main__":
    main()