def calculate_average(marks):
    return sum(marks) / len(marks)

def calculate_average_marks(students):
    return {name: calculate_average(marks) for name, marks in students.items()}

def find_top_performer(average_marks):
    return max(average_marks, key=average_marks.get)
students = {
    "John": [85, 78, 92],
    "Alice": [88, 79, 95],
    "Bob": [70, 75, 80]
}
average_marks = calculate_average_marks(students)
top_performer = find_top_performer(average_marks)
print(f"Average Marks: {average_marks}")
print(f"Top Performer: \"{top_performer}\"")
