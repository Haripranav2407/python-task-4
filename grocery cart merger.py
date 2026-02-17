day1_cart = {
    "apple": 2,
    "banana": 3,
    "orange": 1
}
day2_cart = {
    "banana": 2,
    "orange": 4,
    "grapes": 5
}
merged_cart = {}
for item, qty in day1_cart.items():
    merged_cart[item] = merged_cart.get(item, 0) + qty
for item, qty in day2_cart.items():
    merged_cart[item] = merged_cart.get(item, 0) + qty
print(merged_cart)