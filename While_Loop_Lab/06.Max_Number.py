import sys
max_number = - sys.maxsize

while True:
    line = input()
    if line == "Stop":
        break
    number = int(line)
    if number > max_number:
        max_number = number

print(max_number)
