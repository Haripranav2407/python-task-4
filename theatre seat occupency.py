bookings = {
    "10AM": {1, 2, 3, 4},
    "1PM":  {1, 2, 3},
    "4PM":  {1, 2, 3, 4}
}
all_seats = {1, 2, 3, 4}
fully_booked = []
for show, seats in bookings.items():
    if seats == all_seats:
        fully_booked.append(show)
common_seats = None
for seats in bookings.values():
    if common_seats is None:
        common_seats = seats.copy()
    else:
        common_seats &= seats
print("Fully booked shows:")
print(fully_booked)
print("\nSeats booked in every show:")
print(common_seats)