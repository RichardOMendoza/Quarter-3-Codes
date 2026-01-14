names = ["Me", "Lia", "Jake"]

steps = [
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
]


totals = [sum(person) for person in steps]

max_steps = max(totals)
min_steps = min(totals)

highest_person = names[totals.index(max_steps)]

print("Total steps per person:")
for name, total in zip(names, totals):
    print(f"{name}: {total}")

print("\nHighest total steps:", highest_person, "-", max_steps)
print("Difference between highest and lowest:", max_steps - min_steps)
