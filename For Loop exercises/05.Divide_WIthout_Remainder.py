n = int(input())
group1 = 0
group2 = 0
group3 = 0
for i in range(1, n+1):
    number = int(input())
    if number % 2 == 0:
        group1 += 1
    if number % 3 == 0:
        group2 += 1
    if number % 4 == 0:
        group3 += 1

print(f"{group1/n*100:.2f}%")
print(f"{group2/n*100:.2f}%")
print(f"{group3/n*100:.2f}%")