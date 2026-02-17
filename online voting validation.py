votes = [
    (101, "Alice"),
    (102, "Bob"),
    (103, "Alice"),
    (101, "Charlie"),
    (104, "Bob"),
    (102, "Bob")
]
voted = set()
invalid_votes = []
vote_count = {}
for voter_id, candidate in votes:
    if voter_id in voted:
        invalid_votes.append((voter_id, candidate))
    else:
        voted.add(voter_id)
        vote_count[candidate] = vote_count.get(candidate, 0) + 1
print("Invalid votes:")
print(invalid_votes)
print("\nFinal vote count per candidate:")
print(vote_count)