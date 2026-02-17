preferences = {
    "Alice": {"Bob", "Charlie"},
    "Bob": {"Alice"},
    "Charlie": set(),
    "David": {"Alice"},
    "Eva": set()
}
mutual = []
for student, chosen in preferences.items():
    for other in chosen:
        if other in preferences and student in preferences[other]:
            pair = tuple(sorted((student, other)))
            if pair not in mutual:
                mutual.append(pair)
chosen_by_anyone = set()
for chosen in preferences.values():
    chosen_by_anyone |= chosen
isolated_students = [s for s in preferences if s not in chosen_by_anyone]
print("Mutual preferences:")
print(mutual)
print("\nIsolated students:")
print(isolated_students)