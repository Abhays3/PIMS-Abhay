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

def calculate_fine(speed_over):
    """
    calculates fine amount based on speed over limit.
    parameters: speed_over (int)
    Returns: fine amount in dollars (int)
    
    """
    if 1 <= speed_over<= 10:
        return 30
    elif 11 <= speed_over<= 20:
        return 80
    elif 21 <= speed_over <= 30:
        return 170
    elif 31 <= speed_over <= 40:
        return 400
    else:
        return 630
    
def check_warrant(driver_name):
    """
    Checks if driver name is on wanted list (case-insensitive).
    parameters: driver_name (str)
    Returns: True if wantede, False otherwise
    
    """
    for wanted_person in WANTED_LIST:
        if driver_name.lower() == wanted_person.lower():
            return True
        return False

def validate_licence(licence):
    """
    Validates driver licence format format: 2 letters followed by 6 digits
    Returns True if valid, False otherwise
    
    """
    if len(licence) != 8:
        return False
    
    letters = licence[:2]
    digits = licence[2:]
    
    return letters.isalpha and digits.isdigit()

def record_offence():
    """
    Collects, validates, and stores a new speeding offence record.
    
    """
    print("\n--- Record Speeding Offence ---")
    
    # 1. Driver Name Validation
    while True:
        name = input("Enter driver's full name: ").strip().title()
        if len(name) > 0:
            break
        print("Error Driver name cannot be empty.")
    
    # 2. Driver Licence Validation
    while True:
        licence = input("Enter licence number: ").strip().upper()
        if validate_licence(licence):
            break
        print("Error: Licence must be 2 letters followed by 6 digits")
        
    #3. Posted Speed limit Validation
    while True:
        limit_input = input("Enter posted speed limit (30 - 11- km/h): ").strip()
        if limit_input.isdigit():
            limit = int(limit_input)
            if 30 <= limit <= 110:
                break
            print("Error: Speed limit must be between 30 and 110 km/h.")
        else:
            print("Error: Please enter a valid numeric speed limit.")
            
    #4. Recorded Speed Validation
    while True:
        speed_input = input("Enter recorded speed (km/h): ").strip()
        if speed_input.isdigit():
            speed = int(speed_input)
            if speed > limit:
                break
            else:
                print(f"No speeding offene occurred! Recorded speed ({speed}) is not above limit ({limit}).")
        else:
            print("Error: Please enter a valid speed.")
            
            # Calculate Speed Over & Fine Amount
            speed_over = speed - limit
            fine = calculate_fine(speed_over)
            
            # Store record as a dictionary in our multidimensional lisr
            record = {
                "driver": name,
                "licence": licence,
                "limit": limit,
                "speed": speed,
                "over": speed_over,
                "fine": fine
                
            }
            
            offence_records.append(record)
            
            # Output fine details
            print("\n--- OFFENCE RECORDED ---")
            print(f"Driver: {name} Licence: {licence}")
            print(f"speed over limit: {speed_over} km/h")
            print(f"Calculated Fine: ${fine}")
            
            # Automated Warrant Check
            if check_warrant(name):
                print("\n" + "!" * 40)
                print(f" WARNING: {name.upper()} IS ON THE WANTED LIST!")
                print("  PLEASE TAKE POLICE ACTION.")
                print("!" * 40)
                
    


def display_menu():
    """Displays the main menu options for the officer."""
    print("\n" + "=" * 30)
    print("     Police Patrol System    ")
    print("=" * 30)
    print("1. Record a speeding offence")
    print("2. View all recorded offences")
    print("3. Search offence records")
    print("4. Display patrol summary")
    print("5. Exit program")
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
            
    
    