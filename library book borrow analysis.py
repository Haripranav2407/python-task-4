borrow_records = [
    {"student": "Alice", "book": "Python", "days": 5},
    {"student": "Bob", "book": "Java", "days": 10},
    {"student": "Alice", "book": "Python", "days": 12},
    {"student": "Charlie", "book": "C++", "days": 7},
    {"student": "Bob", "book": "Python", "days": 3}
]
students_more_than_7 = set()
book_count = {}
for record in borrow_records:
    student = record["student"]
    book = record["book"]
    days = record["days"]
    if days > 7:
        students_more_than_7.add(student)
    book_count[book] = book_count.get(book, 0) + 1
print("Students who borrowed books for more than 7 days:")
print(students_more_than_7)
print("\nBook borrow count:")
print(book_count)