print("\nSummary of Grades:\n")

total_all = 0
highest = students[0]["grade"]
lowest = students[0]["grade"]

for student in students:
    grade = student["grade"]
    
    total_all += grade
    
    if grade > highest:
        highest = grade
    if grade < lowest:
        lowest = grade

average_all = total_all / len(students)

print("Total of all grades:", total_all)
print("Average grade:", average_all)
print("Highest grade:", highest)
print("Lowest grade:", lowest)
