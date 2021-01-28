n = int(input())
counter = 0
for first_num in range(n + 1):
    for second_num in range(n + 1):
        for third_num in range(n + 1):
            if first_num + second_num + third_num == n:
                counter +=1

print(counter)