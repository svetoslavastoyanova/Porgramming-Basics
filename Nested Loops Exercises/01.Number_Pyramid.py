n = int(input())
current = 1
is_bigger = False

for row in range(1, n + 1):
    for col in range(row):
        print(f"{current}", end=" ")
        current += 1
        if current > n:
            is_bigger = True
            break
    if is_bigger == True: # ili samo if is_bigger
        break
    print()