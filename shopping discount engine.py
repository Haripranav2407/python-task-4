purchases = {
    "Alice": 4500,
    "Bob": 7000,
    "Charlie": 12000
}
final_amounts = {}
for customer, amount in purchases.items():
    if amount > 10000:
        final_amounts[customer] = amount * 0.80   
    elif amount > 5000:
        final_amounts[customer] = amount * 0.90  
    else:
        final_amounts[customer] = amount
print(final_amounts)