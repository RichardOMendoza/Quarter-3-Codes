names = ["Me", "Lia", "Jake"]

steps = [
    [4500, 5200, 4800, 5000, 5300],  # Me
    [4000, 4100, 3900, 4200, 4600],  # Lia
    [6000, 5800, 5900, 6100, 6200]   # Jake
]

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]



daily_totals = []

for day_index in range(len(days)):
    day_total = 0
    for person in steps:
        day_total += person[day_index]
    daily_totals.append(day_total)
    print(f"{days[day_index]} total steps: {day_total}")

most_active_day = days[daily_totals.index(max(daily_totals))]

print("\nMost active day overall:", most_active_day)
