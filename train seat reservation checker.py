reservations = [
    ("A", 1),
    ("A", 2),
    ("B", 1),
    ("A", 1),
    ("B", 2),
    ("B", 1),
    ("C", 5)
]
seen = set()
duplicates = []
coach_seats = {}
for coach, seat in reservations:
    booking = (coach, seat)
    if booking in seen:
        duplicates.append(booking)
    else:
        seen.add(booking)
    if coach not in coach_seats:
        coach_seats[coach] = set()
    coach_seats[coach].add(seat)
unique_seat_count = {c: len(s) for c, s in coach_seats.items()}
print("Duplicate seat bookings:")
print(duplicates)
print("\nTotal unique seats booked per coach:")
print(unique_seat_count)