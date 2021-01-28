student_name = input()
yearly_grades = 0
grades_count = 0
bad_grades = 0

for i in range(12):
    current_grade = float(input())
    yearly_grades += current_grade

    if current_grade < 4:
        bad_grades += 1

    if bad_grades >= 2:
        print(f"{student_name} has been excluded at {grades_count} grade")
        break

    grades_count += 1

if bad_grades <= 1:
    average_grade = yearly_grades / grades_count
    print(f"{student_name} graduated. Average grade: {average_grade:.2f}")




