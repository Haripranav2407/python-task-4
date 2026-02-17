entries = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78),
    ("Alice", 90),
    ("David", 88)
]
seen_players = set()
invalid_entries = []
valid_entries = []
for player, score in entries:
    if player in seen_players:
        invalid_entries.append((player, score))
    else:
        seen_players.add(player)
        valid_entries.append((player, score))
leaderboard = sorted(valid_entries, key=lambda x: x[1], reverse=True)
print("Invalid entries (duplicate players):")
print(invalid_entries)
print("\nFinal sorted leaderboard:")
print(leaderboard)