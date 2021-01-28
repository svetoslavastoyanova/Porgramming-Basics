bad_grades = int(input())
bad_grades_count = 0
total_grades_count = 0
grades_sum = 0
last_name = ""

while True:
    name = input()

    if name == "Enough":
        print(f"Average score: {grades_sum/total_grades_count:.2f}")
        print(f"Number of problems: {total_grades_count}")
        print(f"Last problem: {last_name}")
        break

    last_name = name
    current_grade = int(input())
    total_grades_count += 1
    grades_sum += current_grade

    if current_grade <= 4:
        bad_grades_count += 1

    if bad_grades_count == bad_grades:
        print(f"You need a break, {bad_grades} poor grades.")
        break
