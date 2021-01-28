import sys
n = int(input())
max_number = - sys.maxsize
total_sum = 0

for i in range(n):
    number = int(input())

    if number > max_number:
        max_number = number

    total_sum += number
total_sum -= max_number
if total_sum == max_number:
    print(f"Yes")
    print(f"Sum = {max_number}")
else:
    diff = abs(total_sum - max_number)
    print(f"No")
    print(f"Diff = {diff}")
