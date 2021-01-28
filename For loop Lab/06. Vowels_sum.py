text = input()
sum = 0

for index in range(0, len(text)):
    symbol = text[index]

    if symbol == "a":
        sum += 1
    elif symbol == "e":
        sum += 2
    elif symbol == "i":
        sum += 3
    elif symbol == "o":
        sum += 4
    elif symbol == "u":
        sum += 5

print(sum)