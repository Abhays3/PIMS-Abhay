# Patrol Car Infringement Management System (PIMS)


WANTED_LIST = [
    "Abhay Singh",
    "Spider Man",
    "Super Man",
    "Tony Stark",
    "Shawn Jonathan"
]

# List collection to store all recorded offence dictionaries
offence_records = []


def calculate_fine(speed_over):
    """
    Calculates fine amount based on speed over limit.
    Parameters: speed_over (int)
    Returns: fine amount in dollars (int)
    """
    if 1 <= speed_over <= 10:
        return 30
    elif 11 <= speed_over <= 20:
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
    Parameters: driver_name (str)
    Returns: True if wanted, False otherwise
    """
    for wanted_person in WANTED_LIST:
        if driver_name.lower() == wanted_person.lower():
            return True
    return False


def validate_licence(licence):
    """
    Validates driver licence format: 2 letters followed by 6 digits
    Returns True if valid, False otherwise
    """
    if len(licence) != 8:
        return False
    
    letters = licence[:2]
    digits = licence[2:]
    
    return letters.isalpha() and digits.isdigit()


def record_offence():
    """Collects, validates, and stores a new speeding offence record."""
    print("\n--- Record Speeding Offence ---")
    
    # 1. Driver Name Validation
    while True:
        name = input("Enter driver's full name: ").strip().title()
        if len(name) > 0:
            break
        print("Error: Driver name cannot be empty.")
    
    # 2. Driver Licence Validation
    while True:
        licence = input("Enter licence number: ").strip().upper()
        if validate_licence(licence):
            break
        print("Error: Licence must be 2 letters followed by 6 digits.")
        
    # 3. Posted Speed Limit Validation
    while True:
        limit_input = input("Enter posted speed limit (30 - 110 km/h): ").strip()
        if limit_input.isdigit():
            limit = int(limit_input)
            if 30 <= limit <= 110:
                break
            print("Error: Speed limit must be between 30 and 110 km/h.")
        else:
            print("Error: Please enter a valid numeric speed limit.")
            
    # 4. Recorded Speed Validation
    while True:
        speed_input = input("Enter recorded speed (km/h): ").strip()
        if speed_input.isdigit():
            speed = int(speed_input)
            if speed > limit:
                break
            else:
                print(f"No speeding offence occurred! Recorded speed ({speed}) is not above limit ({limit}).")
                return
        else:
            print("Error: Please enter a valid speed.")
            
    # Calculate Speed Over & Fine Amount
    speed_over = speed - limit
    fine = calculate_fine(speed_over)
    
    # Store record as a dictionary in our list
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
    print(f"Driver: {name} | Licence: {licence}")
    print(f"Speed over limit: {speed_over} km/h")
    print(f"Calculated Fine: ${fine}")
    
    # Automated Warrant Check
    if check_warrant(name):
        print("\n" + "!" * 40)
        print(f" WARNING: {name.upper()} IS ON THE WANTED LIST!")
        print("  PLEASE TAKE POLICE ACTION.")
        print("!" * 40)


def view_all_offences():
    """Displays all recorded offences in a formatted table layout."""
    print("\n--- Recorded Offences ---")
    
    if not offence_records:
        print("No offences recorded during this patrol shift.")
        return
    
    # Print Table Headers
    print(f"{'Driver':<18} {'Licence':<12} {'Limit':<8} {'Speed':<8} {'Over':<8} {'Fine'}")
    print("-" * 65)
    
    # Iterate and display each record
    for record in offence_records:
        print(f"{record['driver']:<18} {record['licence']:<12} {record['limit']:<8} "
              f"{record['speed']:<8} {record['over']:<8} ${record['fine']}")


def search_offences():
    """Searches for offence records using driver full name or licence number."""
    print("\n--- Search Offence Records ---")
    
    if not offence_records:
        print("No offences recorded to search.")
        return
    
    search_query = input("Enter driver's full name or licence number: ").strip().lower()
    matches = []
    
    # Search algorithm checking name or licence
    for record in offence_records:
        if search_query == record['driver'].lower() or search_query == record['licence'].lower():
            matches.append(record)
            
    if matches:
        print(f"\nFound {len(matches)} matching record(s):")
        print(f"{'Driver':<18} {'Licence':<12} {'Limit':<8} {'Speed':<8} {'Over':<8} {'Fine'}")
        print("-" * 65)
        for record in matches:
            print(f"{record['driver']:<18} {record['licence']:<12} {record['limit']:<8} "
                  f"{record['speed']:<8} {record['over']:<8} ${record['fine']}")
    else:
        print(f"No matching records found for query: '{search_query}'")


def display_summary():
    """Displays shift statistics: total offences, total fines, average speed over limit, highest offence."""
    print("\n--- PATROL SUMMARY ---")
    
    if not offence_records:
        print("No offences recorded during this shift.")
        return
    
    total_offences = len(offence_records)
    total_fines = sum(record['fine'] for record in offence_records)
    
    # Calculate Average Speed over Limit
    total_over = sum(record['over'] for record in offence_records)
    avg_over = round(total_over / total_offences, 1)
    
    # Find Highest Speeding Offence using loop tracking
    highest_record = offence_records[0]
    for record in offence_records:
        if record['over'] > highest_record['over']:
            highest_record = record
            
    print(f"Total offences:           {total_offences}")
    print(f"Total fines issued:       ${total_fines:,}")
    print(f"Average speed over limit: {avg_over} km/h")
    print(f"Highest offence:          {highest_record['driver']} ({highest_record['over']} km/h over)")


def display_menu():
    """Displays the main menu options for the officer."""
    print("\n" + "=" * 30)
    print("    Police Patrol System    ")
    print("=" * 30)
    print("1. Record a speeding offence")
    print("2. View all recorded offences")
    print("3. Search offence records")
    print("4. Display patrol summary")
    print("5. Exit program")
    print("=" * 30)


def main():
    """Main Program execution loop."""
    running = True
    
    while running:
        display_menu()
        choice = input("Select an option (1-5): ").strip()
        
        if choice == "1":
            record_offence()
        elif choice == "2":
            view_all_offences()
        elif choice == "3":
            search_offences()
        elif choice == "4":
            display_summary()
        elif choice == "5":
            print("\nExiting PIMS. Stay safe!")
            running = False
        else:
            print("\nInvalid choice. Please select a number between 1 and 5.")


if __name__ == "__main__":
    main()