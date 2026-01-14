temperatures = [
    [30, 31, 29, 28, 30, 32, 33],  # City A
    [25, 26, 24, 23, 25, 27, 28]   # City B
]

for i, city in enumerate(temperatures):
    print(f"City {i + 1} temperatures:", city)
    print("Total:", sum(city))
    print("Average:", sum(city) / len(city))
    print()

print("Maximum temperature overall:", max(max(city) for city in temperatures))

Using a 2D array made it easier to organize and analyze the temperature data because each city’s data was grouped into its own row. 
This structure allowed me to loop through the data efficiently and calculate totals and averages without repeating code. 
Finding the total and average for each row was straightforward using built-in functions like sum() and len(). 
The slightly more challenging part was finding the maximum value across the entire dataset, since it required checking all rows together.
