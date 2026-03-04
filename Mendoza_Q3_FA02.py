temperatures = [
    [30, 31, 29, 28, 30, 32, 33],  # City A
    [25, 26, 24, 23, 25, 27, 28]   # City B
]

print(temperatures[0][2])          # Access City A's temperature on Wednesday
temperatures[1][5] = 29            # Update City B's temperature on Saturday
print(sum(temperatures[0]) / 7)    # Average temperature of City A
