bids = [
    ("B1", 500),
    ("B2", 700),
    ("B1", 800),
    ("B3", 650),
    ("B2", 900),
    ("B1", 750)
]
highest_per_bidder = {}
for bidder, amount in bids:
    if bidder not in highest_per_bidder:
        highest_per_bidder[bidder] = amount
    else:
        highest_per_bidder[bidder] = max(highest_per_bidder[bidder], amount)
top_bidder = max(highest_per_bidder, key=highest_per_bidder.get)
print("Highest bid per bidder:")
print(highest_per_bidder)
print("\nBidder with highest single bid overall:")
print(top_bidder, "->", highest_per_bidder[top_bidder])