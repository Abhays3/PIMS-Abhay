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
    
    
def main():
    """Main Program excution loop."""
    running = True
    
    while running:
        display_menu()
        choice = input("Select an option (1-5): ").strip()
        
        if choice == "1":
            print("\n[Feature coming soon: Record Offence]")
        elif choice == "2":
            print("\n[Feature coming soon: View Offences]")
        elif choice == "3":
            print("\n[Feature coming soon: Search Records]")
        elif choice == "4":
            print("\n[Feature coming soon: Patrol Summary]")
        elif choice == "5":
            print("\n[Exiting PIMS.: Stay safe!]")
            running = false
        else:
            print("\nInvalid Choice. Please select a number between 1 and 5.")
            
if __name__ == "__main__":
    main()
            
    
    