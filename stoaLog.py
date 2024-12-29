'''
Objective: Create a user-friendly application for maintaining a personal journal. The journal should allow users to log daily reflections, view past entries, and search through them easily. It should focus on simplicity, privacy, and flexibility.

Key Features
	1.	Add Entries:
	    automatically apply date and time for new entry, user types in title and entry and exxit using EOFError

	    automatically sort entries based upon date and time

	2.	Delete Entries:
	    Delete Entries: Remove unwanted entries.

	3.  View Entries:
	    Display all entries in chronological order, formatted for readability.

	4.	Search Functionality:
	    Search by keywords or specific dates.

	5.	Data Persistence:
	    Save journal entries in a structured file format (e.g., JSON or SQLite).
'''

import json
import sys
from datetime import datetime

journal = {}
# journal = {"date-time": {"title": "entry"}}

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
    entry = input("Entry: ")

    journal[date_time] = {"title": title, "entry": entry}
    print(f"\n{title} has been added to journal")

def delete_entry():
    pass

def view_entry():
    pass

def search_journal():
    pass

def save_journal():
    pass


if __name__ == "__main__":
    main()