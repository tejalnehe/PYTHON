def calculate_average(marks):
    total_marks = sum(marks)
    average = total_marks / len(marks)
    return average
subject1 = float(input("Enter marks for subject 1: "))
subject2 = float(input("Enter marks for subject 2: "))
subject3 = float(input("Enter marks for subject 3: "))
average_marks = calculate_average(marks_list)
print(f"The average marks for the three subjects is: {average_marks}")