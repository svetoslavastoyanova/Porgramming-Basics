line = input()
student_tickets = 0
standard_tickets = 0
kid_tickets = 0
total_tickets = 0

while line != "Finish":
    available_seats = int(input())
    ticket_type = input()
    movie_tickets = 0
    while ticket_type != "End":
        total_tickets += 1
        movie_tickets += 1
        if ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
        else:
            kid_tickets += 1

        if movie_tickets == available_seats:
            break
        ticket_type = input()

    percentage = movie_tickets/available_seats*100
    print(f"{line} - {percentage:.2f}% full.")
    line = input()

print(f"Total tickets: {total_tickets}")

percent_student = student_tickets/total_tickets*100
print(f"{percent_student:.2f}% student tickets.")

percent_standard = standard_tickets/total_tickets*100
print(f"{percent_standard:.2f}% standard tickets.")

percent_kid = kid_tickets/total_tickets*100
print(f"{percent_kid:.2f}% kids tickets.")