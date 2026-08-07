# Patrol Car Infringement Management System (PIMS)


WANTED_LIST = [
    "Abhay Singh",
    "Spider Man",
    "Super Man",
    "Tony Stark",
    "Shawn Jonathan"
    
]

#list collection to store all recorded offence dictionaries
offence_records = []

def display_menu():
    """Displays the main menu options for the officer."""
    print("\n" + "=" * 30)
    print("     Police Patrol System    ")
    print("=" * 30)
    print("1. Record a speeding offence")
    print("2. View all recorded offences")
    print("3. Search offence records")
    print("4. Display patrol summary")
    print("5. Exist program")
    print("=" * 30)
    
    