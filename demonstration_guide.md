# Demonstration Guide — Smart Bus Ticket Booking & Reservation System

## 1. Launch

Open a terminal in the project folder and run:

```bash
python main.py
```

The welcome message and menu should appear.

## 2. Demonstrate the Five Routes

Choose:

```text
1
```

Show that the application lists R101 through R105 with:

- Route ID
- Journey
- Departure time
- Fare
- Seat capacity
- Status

## 3. Demonstrate Route Search

Choose:

```text
2
```

Enter:

```text
Hyderabad
```

Expected matching routes:

- R101: Karachi -> Hyderabad
- R103: Hyderabad -> Mirpur Khas
- R105: Sukkur -> Hyderabad

Then search:

```text
Atlantis
```

Expected result:

```text
No matching route found.
```

## 4. Demonstrate a Successful Booking

Choose:

```text
3
```

Enter:

```text
Passenger name: Ahmed
Passenger age: 24
Route ID: R101
Number of seats: 2
```

Expected:

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

Explain:

`1200 × 2 = 2400`

## 5. Verify Seat Update

Choose:

```text
1
```

R101 should now show:

```text
38/40
```

This proves that two seats were deducted after a valid booking.

## 6. View Booking History

Choose:

```text
4
```

The booking should appear with:

```text
B1001
Ahmed
R101
2 seats
Rs. 2,400
Confirmed
```

## 7. Demonstrate Cancellation

Choose:

```text
5
```

Enter:

```text
B1001
```

Expected:

```text
Booking B1001 has been cancelled.
Seats restored: 2
Route R101 available seats: 40
```

Explain that the record is retained rather than deleted.

## 8. Prove Double Cancellation Is Prevented

Choose option 5 again and enter:

```text
B1001
```

Expected:

```text
Cancellation rejected: this booking is already cancelled.
```

Explain that the route remains at 40 available seats, so restoration happens only once.

## 9. Generate a Report

Choose:

```text
7
```

After the cancellation above, the report should show:

```text
Total bookings created: 1
Confirmed bookings: 0
Cancelled bookings: 1
Seats currently reserved: 0
Confirmed revenue: Rs. 0
```

This demonstrates that cancelled fare is excluded from confirmed revenue.

## 10. Demonstrate Invalid Input

### Invalid menu

Enter:

```text
99
```

Expected:

```text
Invalid choice. Please enter a number from 1 to 9.
```

### Zero seats

Start a booking and enter:

```text
Number of seats: 0
```

Expected rejection with no seat change.

### Too many seats

Request more seats than the route currently has.

Expected rejection and no negative availability.

## 11. Demonstrate Schedule

Choose:

```text
8
```

The schedule is grouped by departure city. Karachi should show R101, R102, and R104; Hyderabad should show R103; Sukkur should show R105.

## 12. How to Explain the Code

### `routes`

A list of dictionaries stores route details.

### `bookings`

A list of dictionaries stores reservation records.

### `issued_booking_ids`

A set prevents duplicate booking IDs.

### `SUPPORTED_CITIES`

A tuple stores the supported city collection.

### Booking flow

1. Read passenger name.
2. Validate name.
3. Read and validate age.
4. Find route.
5. Read and validate seat quantity.
6. Check availability.
7. Generate a unique ID.
8. Calculate fare.
9. Save the booking.
10. Decrease available seats.

### Cancellation flow

1. Find the booking.
2. Check whether it exists.
3. Check whether status is Confirmed.
4. Restore its seats.
5. Change status to Cancelled.
6. Keep the record in history.

### Report flow

The program counts all records, separates Confirmed and Cancelled records, sums seats and fares for Confirmed bookings only, and counts routes with zero available seats.

## 13. Short Presentation Outline

1. Project title
2. Problem statement
3. Objectives
4. Scope and constraints
5. Main features
6. Data structures
7. Booking workflow
8. Cancellation workflow
9. Report calculations
10. Testing
11. Limitations
12. Conclusion

## 14. Likely Instructor Questions

### Q1. Why did you use a list of dictionaries?

**Answer:** A list stores multiple records, while each dictionary keeps related fields together using readable names.

### Q2. Why is a set used?

**Answer:** The set tracks issued booking IDs and helps prevent duplicate IDs.

### Q3. Why is a tuple used?

**Answer:** The supported city collection is fixed for the application, so a tuple is appropriate.

### Q4. Why are bookings stored in memory?

**Answer:** The PRD explicitly requires in-memory storage and excludes databases and persistence.

### Q5. How do you prevent overbooking?

**Answer:** The requested seat quantity is compared with the route's available seats before the booking is created or seats are changed.

### Q6. What happens when a booking is cancelled?

**Answer:** Its status changes from Confirmed to Cancelled, its seats are restored once, and the booking remains in history.

### Q7. Why is cancelled revenue excluded?

**Answer:** The PRD defines confirmed revenue as the sum of fares from Confirmed bookings only.

### Q8. How do you prevent double restoration?

**Answer:** Cancellation checks the booking status. A booking whose status is already Cancelled is rejected.

### Q9. What happens after the program closes?

**Answer:** All records are lost because the project uses in-memory storage only.

### Q10. Which Python concepts are demonstrated?

**Answer:** Lists, dictionaries, tuples, sets, conditions, loops, nested loops, `for-else`, `break`, `continue`, `enumerate()`, validation, and arithmetic calculations.
