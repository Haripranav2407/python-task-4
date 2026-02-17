orders = [
    {"order_id": 1, "restaurant": "R1", "items": ["Burger", "Fries"]},
    {"order_id": 2, "restaurant": "R2", "items": ["Pizza", "Pizza"]},
    {"order_id": 3, "restaurant": "R1", "items": []},
    {"order_id": 4, "restaurant": "R3", "items": ["Pasta", "Salad"]},
    {"order_id": 5, "restaurant": "R2", "items": ["Burger", "Burger"]}
]
all_have_items = True
for order in orders:
    if not order["items"]:
        all_have_items = False
        break
duplicate_item_restaurants = set()
for order in orders:
    items = order["items"]
    if len(items) != len(set(items)):
        duplicate_item_restaurants.add(order["restaurant"])
print("Every order has at least one item:")
print(all_have_items)
print("\nRestaurants with duplicate item orders:")
print(duplicate_item_restaurants)