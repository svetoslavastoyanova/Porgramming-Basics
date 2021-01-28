n = int(input())

group1 = 0
group2 = 0
group3 = 0
group4 = 0
group5 = 0

for i in range (1, n+1):
    number = int(input())
    if number < 200:
        group1 += 1
    elif 200 <= number <= 399:
        group2 += 1
    elif 400 <= number <= 599:
        group3 += 1
    elif 600 <= number <= 799:
        group4 += 1
    elif number >= 800:
        group5 += 1

print(f"{group1/n*100:.2f}%")
print(f"{group2/n*100:.2f}%")
print(f"{group3/n*100:.2f}%")
print(f"{group4/n*100:.2f}%")
print(f"{group5/n*100:.2f}%")