# Smart Bus Ticket Booking & Reservation System

## 1. Project Overview

The **Smart Bus Ticket Booking & Reservation System** is a beginner-friendly Python 3 console application for managing bus routes, ticket bookings, cancellations, seat availability, schedules, and booking reports.

The project follows the uploaded Product Requirements Document (PRD). The PRD defines the application as a text-based Python application with in-memory records, no database, no GUI, no external APIs, and no third-party libraries.

## 2. Problem Statement

Manual reservation processes can cause duplicate bookings, incorrect seat counts, fare errors, and reports that incorrectly count cancelled tickets as revenue.

This application provides a consistent console workflow for viewing routes, searching journeys, booking seats, cancelling bookings, checking availability, and generating reports.

## 3. Objectives

- Display scheduled routes and seat availability.
- Search routes by route ID, departure city, or destination city.
- Validate passenger and booking information.
- Generate unique booking IDs.
- Calculate fares consistently.
- Keep seat availability synchronized with confirmed bookings.
- Cancel confirmed bookings and restore seats exactly once.
- Keep cancelled records in booking history.
- Exclude cancelled bookings from confirmed revenue.
- Demonstrate beginner Python concepts such as lists, dictionaries, tuples, sets, loops, `for-else`, `break`, `continue`, and `enumerate()`.

## 4. Scope

### In scope

- Python 3 console application
- In-memory route and booking records
- Route search
- Ticket booking
- Cancellation
- Seat availability
- Schedule display
- Booking reports
- Input validation
- Testing

### Out of scope

- GUI
- Website or mobile application
- Database
- Persistent storage
- Payment gateway
- External API
- Third-party Python packages

## 5. Technology

- **Language:** Python 3
- **Libraries:** Built-in Python functionality only
- **Interface:** Console
- **Storage:** In memory

## 6. Sample Routes

| Route | Departure | Destination | Time | Fare | Capacity |
|---|---|---|---|---:|---:|
| R101 | Karachi | Hyderabad | 08:00 AM | Rs. 1,200 | 40 |
| R102 | Karachi | Sukkur | 09:30 AM | Rs. 2,000 | 36 |
| R103 | Hyderabad | Mirpur Khas | 11:00 AM | Rs. 800 | 32 |
| R104 | Karachi | Lahore | 07:00 PM | Rs. 5,000 | 45 |
| R105 | Sukkur | Hyderabad | 02:00 PM | Rs. 1,500 | 30 |

## 7. Project Files

```text
Smart_Bus_Ticket_Booking_System/
├── main.py
├── README.md
├── test_cases.txt
├── demonstration_guide.md
├── presentation_outline.md
├── screenshots/
│   ├── 01_route_listing.png
│   ├── 02_successful_booking.png
│   ├── 03_cancellation.png
│   └── 04_booking_report.png
└── Smart_Bus_Ticket_Booking_System.zip
```

## 8. Requirements and Setup

Install Python 3.

Check the installation:

```bash
python --version
```

or on some systems:

```bash
python3 --version
```

No external package installation is required.

## 9. Run the Application

From the project folder:

```bash
python main.py
```

The application displays the welcome screen and main menu.

## 10. Main Menu

1. View Available Routes
2. Search for a Route
3. Book a Ticket
4. View My Bookings
5. Cancel a Booking
6. View Seat Availability
7. Generate Booking Report
8. View Route Schedule
9. Exit

The PRD's original menu has eight entries including Exit. This implementation adds the required route-schedule action as a separate menu item because the PRD also explicitly requires route schedules. The core behavior is unchanged.

## 11. Sample Booking Workflow

Example:

```text
Enter your choice: 3
Passenger name: Ahmed
Passenger age: 24
Route ID: R101
Number of seats: 2
```

Expected result:

```text
Booking confirmed!
Booking ID: B1001
Passenger: Ahmed
Route: R101 (Karachi -> Hyderabad)
Seats booked: 2
Fare per seat: Rs. 1,200
Total fare: Rs. 2,400
Status: Confirmed
```

R101 availability changes from `40/40` to `38/40`.

## 12. Cancellation Workflow

If the booking ID is `B1001`:

```text
Enter your choice: 5
Enter booking ID to cancel: B1001
```

The booking remains in history but becomes `Cancelled`, and the two seats are restored.

Trying to cancel `B1001` again is rejected, so the seats are not restored a second time.

## 13. Reports

The booking report shows:

- Total bookings created
- Confirmed bookings
- Cancelled bookings
- Seats currently reserved
- Confirmed revenue
- Fully booked routes

Confirmed revenue and currently reserved seats include **Confirmed** bookings only. Cancelled fare is excluded.

## 14. Data Structures

### List

Used for route and booking collections.

### Dictionary

Each route and booking is represented by a dictionary containing named fields.

### Tuple

`SUPPORTED_CITIES` stores the supported city collection.

### Set

`issued_booking_ids` tracks IDs that have already been issued.

### Strings

Used for names, cities, route IDs, times, and statuses.

### Integers

Used for age, seat counts, capacities, and fares.

### Booleans

Used for logical flags such as search matches and schedule matches.

## 15. Validation Rules

- Passenger name cannot be blank.
- Age must be a positive integer.
- Route ID must exist.
- Seat quantity must be a positive integer.
- Requested seats cannot exceed available seats.
- Invalid input must not change route availability.
- Booking IDs must be unique.
- Only confirmed bookings can be cancelled.
- Cancelled bookings cannot be cancelled again.
- Cancelled records remain visible.
- Cancelled fare is excluded from confirmed revenue.
- Available seats must remain within `0 <= available <= total`.

## 16. Required Python Concepts

The implementation meaningfully demonstrates:

- Variables and data types
- Strings, integers, floats, booleans
- Lists
- Dictionaries
- Tuples
- Sets
- `if`, `elif`, `else`
- Nested conditions
- `for` loops
- Nested `for` loops
- `while` loops
- `for-else` behavior in the route/cancellation search logic
- `break`
- `continue`
- `enumerate()`
- Input validation
- Fare calculations

## 17. Testing

The project includes `test_cases.txt` with the 12 required PRD scenarios.

The automated verification performed during project preparation checks the main business logic, including:

- Initial route data
- Hyderabad search
- Successful R101 booking
- Fare calculation
- Seat decrement
- Invalid zero-seat booking
- Over-capacity booking
- Cancellation
- Double-cancellation protection
- Empty report
- Full route booking
- Revenue exclusion after cancellation
- Invalid menu input

## 18. Storage Limitation

This is intentionally an **in-memory** application.

Bookings and seat changes exist only while the Python process is running. When the application closes, the records are lost. No database or persistence mechanism is included because persistent storage is outside the required PRD scope.

## 19. Future Improvements

These can be considered only after the core project is complete:

- Database persistence
- Individual seat-number assignment
- Passenger-name search
- Revenue by departure city
- Popular-route analysis
- Defined child/adult fare categories
- Optional multi-seat discount

These are not required for the core assignment.

## 20. Instructor Demonstration

Use `demonstration_guide.md` for the complete walkthrough and `presentation_outline.md` for a short presentation structure.

## 21. Important Note

The application is designed to be understandable and defensible by a beginner. The code avoids frameworks and external dependencies so each major operation can be explained directly in terms of Python fundamentals.
