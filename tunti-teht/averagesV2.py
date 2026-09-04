def averages(numbers):
    if not numbers:
        return 0.0
    return round(sum(numbers) / len(numbers), 2)


def average_grade(grade_lists):
    averages_list = []
    for sublist in grade_lists:
        avg = averages(sublist)
        averages_list.append(avg)
    return averages_list


group_count = int(input("How many students' grades will you enter? "))
all_grades = []

for i in range(group_count):
    print(f"\n--- Student {i+1} ---")
    grade_count = int(input("How many grades does this student have? "))

    student_list = []
    for j in range(grade_count):
        grade = float(input(f"Enter grade {j+1}: "))
        student_list.append(grade)

    all_grades.append(student_list)


final_result = average_grade(all_grades)

print("\n--- All Averages ---")
print(final_result)