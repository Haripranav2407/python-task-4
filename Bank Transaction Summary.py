transactions = [
    {"account_id": "A1", "amount": 5000, "type": "CREDIT"},
    {"account_id": "A2", "amount": 3000, "type": "CREDIT"},
    {"account_id": "A1", "amount": 2000, "type": "DEBIT"},
    {"account_id": "A2", "amount": 1000, "type": "DEBIT"},
    {"account_id": "A1", "amount": 1500, "type": "CREDIT"}
]
balances = {}
for tx in transactions:
    acc = tx["account_id"]
    amt = tx["amount"]
    if acc not in balances:
        balances[acc] = 0
    if tx["type"] == "CREDIT":
        balances[acc] += amt
    elif tx["type"] == "DEBIT":
        balances[acc] -= amt

max_account = max(balances, key=balances.get)
print("Final balance per account:")
print(balances)
print("\nAccount with maximum balance:")
print(max_account, "->", balances[max_account])
