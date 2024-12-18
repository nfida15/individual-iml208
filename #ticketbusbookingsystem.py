# Initialize an empty list to store bookings
bookings = []

# Function to create multiple bookings (Create)
def create_booking():
    try:
        # Get the number of tickets to purchase
        num_tickets = int(input("How many tickets do you want to purchase? "))

        if num_tickets <= 0:
            print("Error: Please enter a valid number of tickets.")
            return

        # Loop to get details for each ticket
        for i in range(1, num_tickets + 1):
            print(f"\nEnter details for Ticket {i}:")
            name = input("Enter your name: ")
            age = input("Enter your age: ")
            gender = input("Enter your gender: ")
            ticket_number = input("Enter your ticket number: ")

            # Validate that all fields are filled
            if not name or not age or not gender or not ticket_number:
                print("Error: All fields are required!")
                return

            # Add the booking to the list
            booking = {
                "name": name,
                "age": age,
                "gender": gender,
                "ticket_number": ticket_number
            }
            bookings.append(booking)

        print(f"Success: {num_tickets} ticket(s) have been booked successfully!")

    except ValueError:
        print("Error: Please enter a valid number for tickets.")

# Function to view all bookings (Read)
def view_bookings():
    if not bookings:
        print("No bookings found.")
        return

    print("\nCurrent Bookings:")
    for i, booking in enumerate(bookings, 1):
        print(f"{i}. Ticket Number: {booking['ticket_number']}")
        print(f"   Name: {booking['name']}")
        print(f"   Age: {booking['age']}")
        print(f"   Gender: {booking['gender']}")

# Function to update a booking
def update_booking():
    view_bookings()  # View bookings before updating
    
    try:
        booking_number = int(input("Enter Booking Number to Update: ")) - 1
        if 0 <= booking_number < len(bookings):
            # Get the selected booking
            booking = bookings[booking_number]
            
            # Update details
            print("\nEnter new details (Leave blank to keep current):")
            new_name = input("New Name: ")
            new_age = input("New Age: ")
            new_gender = input("New Gender: ")
            new_ticket_number = input("New Ticket Number: ")

            if new_name:
                booking["name"] = new_name
            if new_age:
                booking["age"] = new_age
            if new_gender:
                booking["gender"] = new_gender
            if new_ticket_number:
                booking["ticket_number"] = new_ticket_number

            print("Success: Booking updated successfully!")
        else:
            print("Error: Invalid booking number!")
    except ValueError:
        print("Error: Please enter a valid number.")

# Function to delete a booking
def delete_booking():
    view_bookings()  # View bookings before deleting
    
    try:
        booking_number = int(input("Enter Booking Number to Delete: ")) - 1
        if 0 <= booking_number < len(bookings):
            del bookings[booking_number]
            print("Success: Booking deleted successfully!")
        else:
            print("Error: Invalid booking number!")
    except ValueError:
        print("Error: Please enter a valid number.")

# Main program loop
def main():
    while True:
        print("\nBus Ticket Booking System")
        print("1. Create Booking")
        print("2. View Bookings")
        print("3. Update Booking")
        print("4. Delete Booking")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            create_booking()
        elif choice == "2":
            view_bookings()
        elif choice == "3":
            update_booking()
        elif choice == "4":
            delete_booking()
        elif choice == "5":
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
