import sys
import string
import random


# Set to store existing booking references to make sure it is unique
existing_references = set()

# Define a function which can produce a random reference
def produce_reference():
    
    while True:
        # Generate a random string of 8 alphanumeric characters
        reference = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        # Check if it is unique by looking up in the existing references set
        if reference not in existing_references:
            existing_references.add(reference)
            return reference
        
class ApachAirlineBookingSystem:
    def __init__(self):
        # Initial configuration of the airplane seating
        # F = Free, R = Reserved, X = Aisle, S = Storage
        self.seats = {
            '1A': 'F', '1B': 'F', '1C': 'F', '1X': 'X', '1D': 'F', '1E': 'F', '1F': 'F',
            '2A': 'F', '2B': 'F', '2C': 'F', '2X': 'X','2D': 'F', '2E': 'F', '2F': 'F', 
            '3A': 'F', '3B': 'F', '3C': 'F', '3X': 'X','3D': 'F', '3E': 'F', '3F': 'F', 
            '4A': 'F', '4B': 'F', '4C': 'F', '4X': 'X','4D': 'F', '4E': 'F', '4F': 'F', 
            '5A': 'F', '5B': 'F', '5C': 'F', '5X': 'X','5D': 'F', '5E': 'F', '5F': 'F', 
            '6A': 'F', '6B': 'F', '6C': 'F', '6X': 'X','6D': 'F', '6E': 'F', '6F': 'F', 
            '7A': 'F', '7B': 'F', '7C': 'F', '7X': 'X','7D': 'F', '7E': 'F', '7F': 'F', 
            '8A': 'F', '8B': 'F', '8C': 'F', '8X': 'X','8D': 'F', '8E': 'F', '8F': 'F', 
            '9A': 'F', '9B': 'F', '9C': 'F', '9X': 'X','9D': 'F', '9E': 'F', '9F': 'F', 
            # .......#
            '78A': 'F', '78B': 'F', '78C': 'F','78X': 'X', '78D': 'S', '78E': 'S', '78F': 'S', 
            '79A': 'F', '79B': 'F', '79C': 'F','79X': 'X', '79D': 'F', '79E': 'F', '79F': 'F', 
            '80A': 'F', '80B': 'F', '80C': 'F','80X': 'X', '80D': 'F', '80E': 'F', '80F': 'F'
        }


    def check_availability(self):
        """Displays all seats and their current booking status."""
        for seat, status in self.seats.items():
            print(f"{seat}: {'Available' if status == 'F' else 'Unavailable'}")

    def book_seat(self):
        """Allows the user to book a seat."""
        seat = input("Enter the seat to book: ")
        if self.seats.get(seat) == 'F':
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            passport_number= input("Enter passport number: ")
            reference = produce_reference()
            # Store a dictionary of booking info in the seat
            self.seats[seat] = {
                "reference": reference,
                "passport_number": passport_number,
                "first_name": first_name,
                "last_name": last_name
            }
            print(f"Seat booked successfully! Reference: {reference}")
        else:
            print("This seat is not available for booking.")

    def free_seat(self):
        """Allows the user to free a reserved seat."""
        seat = input("Enter the seat to free: ")
        if self.seats.get(seat) == 'R':
            self.seats[seat] = 'F'
            print("Seat freed successfully.")
        else:
            print("Seat is not reserved or does not exist.")

    def show_booking_state(self):
        """Shows the current state of all seats."""
        print("Current booking state:")
        for seat, status in self.seats.items():
            if status == 'F':
                print(f"{seat}: Free")
            elif status in ['S', 'X']:
                print(f"{seat}: Non-bookable")
            else:
                print(f"{seat}: Reserved - {status['reference']} ({status['first_name']} {status['last_name']})")

    def exit_program(self):
        """Exits the program."""
        print("Exiting program.")
        sys.exit()

    def menu(self):
        """Shows the menu and handles user input."""
        while True:
            print("\nMenu:")
            print("1. Check availability of seat")
            print("2. Book a seat")
            print("3. Free a seat")
            print("4. Show booking state")
            print("5. Exit program")
            
            choice = input("Enter your choice: ")
            
            if choice == '1':
                self.check_availability()
            elif choice == '2':
                self.book_seat()
            elif choice == '3':
                self.free_seat()
            elif choice == '4':
                self.show_booking_state()
            elif choice == '5':
                self.exit_program()
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

# Create an instance of the ApachAirlineBookingSystem class and start the program
if __name__ == "__main__":
    seating_system = ApachAirlineBookingSystem()
    seating_system.menu()