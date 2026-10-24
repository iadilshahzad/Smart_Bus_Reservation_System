"""
Smart Bus Ticket Booking & Reservation System
Beginner-friendly Python 3 console application.

Requirements:
- Built-in Python only
- In-memory data storage
- Routes, search, booking, cancellation, availability,
  schedules, booking history, and reports
"""

# Tuple: supported departure/destination cities.
SUPPORTED_CITIES = ("Karachi", "Hyderabad", "Sukkur", "Mirpur Khas", "Lahore")

# List of dictionaries: route data stored in memory.
routes = [
    {
        "route_id": "R101",
        "departure_city": "Karachi",
        "destination_city": "Hyderabad",
        "departure_time": "08:00 AM",
        "ticket_price": 1200,
        "total_seats": 40,
        "available_seats": 40,
    },
    {
        "route_id": "R102",
        "departure_city": "Karachi",
        "destination_city": "Sukkur",
        "departure_time": "09:30 AM",
        "ticket_price": 2000,
        "total_seats": 36,
        "available_seats": 36,
    },
    {
        "route_id": "R103",
        "departure_city": "Hyderabad",
        "destination_city": "Mirpur Khas",
        "departure_time": "11:00 AM",
        "ticket_price": 800,
        "total_seats": 32,
        "available_seats": 32,
    },
    {
        "route_id": "R104",
        "departure_city": "Karachi",
        "destination_city": "Lahore",
        "departure_time": "07:00 PM",
        "ticket_price": 5000,
        "total_seats": 45,
        "available_seats": 45,
    },
    {
        "route_id": "R105",
        "departure_city": "Sukkur",
        "destination_city": "Hyderabad",
        "departure_time": "02:00 PM",
        "ticket_price": 1500,
        "total_seats": 30,
        "available_seats": 30,
    },
]

# List of dictionaries: booking records remain in memory.
bookings = []

# Set: prevents duplicate booking IDs.
issued_booking_ids = set()

next_booking_number = 1001


def reset_data():
    """Reset routes and bookings; useful for demonstrations and tests."""
    global routes, bookings, issued_booking_ids, next_booking_number

    routes = [
        {
            "route_id": "R101",
            "departure_city": "Karachi",
            "destination_city": "Hyderabad",
            "departure_time": "08:00 AM",
            "ticket_price": 1200,
            "total_seats": 40,
            "available_seats": 40,
        },
        {
            "route_id": "R102",
            "departure_city": "Karachi",
            "destination_city": "Sukkur",
            "departure_time": "09:30 AM",
            "ticket_price": 2000,
            "total_seats": 36,
            "available_seats": 36,
        },
        {
            "route_id": "R103",
            "departure_city": "Hyderabad",
            "destination_city": "Mirpur Khas",
            "departure_time": "11:00 AM",
            "ticket_price": 800,
            "total_seats": 32,
            "available_seats": 32,
        },
        {
            "route_id": "R104",
            "departure_city": "Karachi",
            "destination_city": "Lahore",
            "departure_time": "07:00 PM",
            "ticket_price": 5000,
            "total_seats": 45,
            "available_seats": 45,
        },
        {
            "route_id": "R105",
            "departure_city": "Sukkur",
            "destination_city": "Hyderabad",
            "departure_time": "02:00 PM",
            "ticket_price": 1500,
            "total_seats": 30,
            "available_seats": 30,
        },
    ]
    bookings = []
    issued_booking_ids = set()
    next_booking_number = 1001


def find_route(route_id):
    """Return a route dictionary for an ID, or None if it does not exist."""
    route_id = route_id.strip().upper()
    for route in routes:
        if route["route_id"] == route_id:
            return route
    return None


def generate_booking_id():
    """Generate a unique booking ID using the issued-ID set."""
    global next_booking_number

    while True:
        booking_id = f"B{next_booking_number}"
        next_booking_number += 1
        if booking_id not in issued_booking_ids:
            issued_booking_ids.add(booking_id)
            return booking_id


def validate_positive_integer(value, field_name):
    """Validate a positive integer entered as text."""
    try:
        number = int(value)
    except ValueError:
        return False, f"{field_name} must be a positive integer."

    if number <= 0:
        return False, f"{field_name} must be greater than zero."

    return True, number


def view_routes(available_only=False):
    """Display all routes or only routes with available seats."""
    print("\nAVAILABLE BUS ROUTES")
    print("-" * 92)
    print(
        f"{'No.':<5}{'Route':<8}{'Journey':<32}"
        f"{'Depart':<13}{'Fare':<14}{'Seats':<10}Status"
    )
    print("-" * 92)

    shown = 0
    for index, route in enumerate(routes, start=1):
        if available_only and route["available_seats"] == 0:
            continue

        shown += 1
        status = (
            "Fully Booked"
            if route["available_seats"] == 0
            else "Available"
        )
        journey = f"{route['departure_city']} -> {route['destination_city']}"
        seats = f"{route['available_seats']}/{route['total_seats']}"
        print(
            f"{index:<5}{route['route_id']:<8}{journey:<32}"
            f"{route['departure_time']:<13}"
            f"Rs.{route['ticket_price']:<11,}{seats:<10}{status}"
        )

    if shown == 0:
        print("No routes match the requested availability filter.")

    print("-" * 92)


def search_route():
    """Search by route ID, departure city, or destination city."""
    search_term = input("Search by route ID or city: ").strip()

    if not search_term:
        print("Search term cannot be empty.")
        return

    normalized = search_term.lower()
    found = False

    for route in routes:
        route_id_match = route["route_id"].lower() == normalized
        departure_match = route["departure_city"].lower() == normalized
        destination_match = route["destination_city"].lower() == normalized

        if route_id_match or departure_match or destination_match:
            print(
                f"{route['route_id']} | "
                f"{route['departure_city']} -> {route['destination_city']} | "
                f"Rs. {route['ticket_price']:,} | "
                f"{route['available_seats']} seats available | "
                f"{route['departure_time']}"
            )
            found = True

            # A unique route ID is enough to identify one route.
            if route_id_match:
                break

    if not found:
        print("No matching route found.")


def book_ticket():
    """Collect, validate, and create a confirmed booking."""
    print("\nBOOK A TICKET")
    print("-" * 30)

    passenger_name = input("Passenger name: ").strip()
    if not passenger_name:
        print("Booking rejected: passenger name cannot be empty.")
        return None

    age_text = input("Passenger age: ").strip()
    age_ok, passenger_age = validate_positive_integer(age_text, "Age")
    if not age_ok:
        print(f"Booking rejected: {passenger_age}")
        return None

    route_id = input("Route ID: ").strip().upper()
    route = find_route(route_id)
    if route is None:
        print("Booking rejected: route ID does not exist.")
        return None

    seats_text = input("Number of seats: ").strip()
    seats_ok, seat_quantity = validate_positive_integer(
        seats_text, "Seat quantity"
    )
    if not seats_ok:
        print(f"Booking rejected: {seat_quantity}")
        return None

    if seat_quantity > route["available_seats"]:
        print(
            f"Booking rejected: only {route['available_seats']} "
            "seat(s) are available."
        )
        return None

    # All validation has passed: now state can safely change.
    booking_id = generate_booking_id()
    total_fare = route["ticket_price"] * seat_quantity

    booking = {
        "booking_id": booking_id,
        "passenger_name": passenger_name,
        "passenger_age": passenger_age,
        "route_id": route["route_id"],
        "seats": seat_quantity,
        "total_fare": total_fare,
        "status": "Confirmed",
    }

    bookings.append(booking)
    route["available_seats"] -= seat_quantity

    print("\nBooking confirmed!")
    print(f"Booking ID: {booking_id}")
    print(f"Passenger: {passenger_name}")
    print(
        f"Route: {route['route_id']} "
        f"({route['departure_city']} -> {route['destination_city']})"
    )
    print(f"Seats booked: {seat_quantity}")
    print(f"Fare per seat: Rs. {route['ticket_price']:,}")
    print(f"Total fare: Rs. {total_fare:,}")
    print("Status: Confirmed")

    return booking_id


def view_bookings():
    """Display every booking, including cancelled records."""
    print("\nMY BOOKINGS")
    print("-" * 90)

    if not bookings:
        print("No bookings found.")
        return

    for index, booking in enumerate(bookings, start=1):
        route = find_route(booking["route_id"])
        journey = "Unknown route"
        if route:
            journey = (
                f"{route['departure_city']} -> {route['destination_city']}"
            )

        print(
            f"{index}. {booking['booking_id']} | "
            f"{booking['passenger_name']} | Age {booking['passenger_age']} | "
            f"{booking['route_id']} ({journey}) | "
            f"Seats: {booking['seats']} | "
            f"Fare: Rs. {booking['total_fare']:,} | "
            f"Status: {booking['status']}"
        )

    print("-" * 90)


def cancel_booking():
    """Cancel one confirmed booking and restore seats exactly once."""
    booking_id = input("Enter booking ID to cancel: ").strip().upper()

    for booking in bookings:
        if booking["booking_id"] == booking_id:
            if booking["status"] == "Cancelled":
                print("Cancellation rejected: this booking is already cancelled.")
                return False

            if booking["status"] == "Confirmed":
                route = find_route(booking["route_id"])

                if route is not None:
                    route["available_seats"] += booking["seats"]

                    # Keep the record for history, but change its status.
                    booking["status"] = "Cancelled"

                    print(f"Booking {booking_id} has been cancelled.")
                    print(f"Seats restored: {booking['seats']}")
                    print(
                        f"Route {route['route_id']} available seats: "
                        f"{route['available_seats']}"
                    )
                    return True

            print("Cancellation rejected: booking is not Confirmed.")
            return False

    print("Booking ID not found.")
    return False


def view_availability():
    """Show available seats and a simple status for every route."""
    print("\nSEAT AVAILABILITY")
    print("-" * 70)

    available_only = input(
        "Show only routes with seats available? (y/n): "
    ).strip().lower()

    for route in routes:
        if available_only == "y" and route["available_seats"] == 0:
            continue

        if route["available_seats"] == route["total_seats"]:
            status = "Available"
        elif route["available_seats"] == 0:
            status = "Fully Booked"
        else:
            status = "Partially Booked"

        print(
            f"{route['route_id']} | "
            f"{route['departure_city']} -> {route['destination_city']} | "
            f"{route['available_seats']}/{route['total_seats']} seats | "
            f"{status}"
        )


def generate_report():
    """Calculate and display booking totals and confirmed revenue."""
    total_bookings = len(bookings)
    confirmed_bookings = 0
    cancelled_bookings = 0
    reserved_seats = 0
    confirmed_revenue = 0
    fully_booked_routes = 0

    for booking in bookings:
        if booking["status"] == "Confirmed":
            confirmed_bookings += 1
            reserved_seats += booking["seats"]
            confirmed_revenue += booking["total_fare"]
        elif booking["status"] == "Cancelled":
            cancelled_bookings += 1

    for route in routes:
        if route["available_seats"] == 0:
            fully_booked_routes += 1

    print("\nBOOKING REPORT")
    print("-" * 45)
    print(f"Total bookings created: {total_bookings}")
    print(f"Confirmed bookings: {confirmed_bookings}")
    print(f"Cancelled bookings: {cancelled_bookings}")
    print(f"Seats currently reserved: {reserved_seats}")
    print(f"Confirmed revenue: Rs. {confirmed_revenue:,}")
    print(f"Fully booked routes: {fully_booked_routes}")

    print("\nCONFIRMED BOOKINGS BY ROUTE")
    print("-" * 45)

    # Nested loops: each route is checked against confirmed bookings.
    for route in routes:
        route_seats = 0
        route_revenue = 0

        for booking in bookings:
            if (
                booking["route_id"] == route["route_id"]
                and booking["status"] == "Confirmed"
            ):
                route_seats += booking["seats"]
                route_revenue += booking["total_fare"]

        if route_seats > 0:
            print(
                f"{route['route_id']}: "
                f"{route_seats} seat(s), Rs. {route_revenue:,}"
            )


def show_schedule():
    """Display route schedules grouped by supported departure city."""
    print("\nROUTE SCHEDULE BY DEPARTURE CITY")
    print("-" * 55)

    for city in SUPPORTED_CITIES:
        print(city)
        found = False

        # Nested loop: scan routes for each supported city.
        for route in routes:
            if route["departure_city"] == city:
                print(
                    f"  {route['route_id']} -> "
                    f"{route['destination_city']} | "
                    f"{route['departure_time']}"
                )
                found = True

        if not found:
            print("  No scheduled departures.")


def show_menu():
    """Display the main menu."""
    print("\nSMART BUS TICKET BOOKING & RESERVATION SYSTEM")
    print("=" * 48)
    print("1. View Available Routes")
    print("2. Search for a Route")
    print("3. Book a Ticket")
    print("4. View My Bookings")
    print("5. Cancel a Booking")
    print("6. View Seat Availability")
    print("7. Generate Booking Report")
    print("8. View Route Schedule")
    print("9. Exit")
    print("=" * 48)


def main():
    """Run the interactive console application."""
    print("\nWelcome to Smart Bus Ticket Booking & Reservation System!")

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_routes()
        elif choice == "2":
            search_route()
        elif choice == "3":
            book_ticket()
        elif choice == "4":
            view_bookings()
        elif choice == "5":
            cancel_booking()
        elif choice == "6":
            view_availability()
        elif choice == "7":
            generate_report()
        elif choice == "8":
            show_schedule()
        elif choice == "9":
            print("Thank you for using Smart Bus Reservation System.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 9.")


if __name__ == "__main__":
    main()
