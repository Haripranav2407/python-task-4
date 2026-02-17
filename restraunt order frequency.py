orders = [
    "Pizza", "Burger", "Pizza",
    "Pasta", "Burger",
    "Salad", "Pizza"
]
dish_count = {}
for dish in orders:
    dish_count[dish] = dish_count.get(dish, 0) + 1
most_ordered = max(dish_count, key=dish_count.get)
ordered_once = []
for dish, count in dish_count.items():
    if count == 1:
        ordered_once.append(dish)
print("Most ordered dish:")
print(most_ordered)
print("\nDishes ordered exactly once:")
print(ordered_once)