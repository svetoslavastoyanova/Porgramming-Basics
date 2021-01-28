jury_counts = int(input())
line = input()
sum_all_grades = 0
count_grades = 0

while line != "Finish":
    sum = 0
    for jury in range(1, jury_counts + 1):
        grade = float(input())
        sum += grade
        sum_all_grades += grade
        count_grades += 1
    average = sum/jury_counts
    print(f"{line} - {average:.2f}.")

    line = input()

average_all_grades = sum_all_grades/count_grades
print(f"Student's final assessment is {average_all_grades:.2f}.")
