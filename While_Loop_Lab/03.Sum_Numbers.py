target_sum = int(input())
current_sum = 0

while True:
    current_number = int(input())
    current_sum += current_number
    if current_sum >= target_sum:
        print(current_sum)
        break