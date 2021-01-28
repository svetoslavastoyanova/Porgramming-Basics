detergent = int(input())
detergent *= 750

pots = 0
dishes = 0
counter = 1

while detergent > 0:
    line = input()
    if line == "End":
        print(f"Detergent was enough!")
        print(f"{dishes} dishes and {pots} pots were washed.")
        print(f"Leftover detergent {detergent} ml.")
        break

    if counter % 3 == 0:
        detergent -= int(line)*15
        pots += int(line)

    else:
        detergent -= int(line)*5
        dishes += int(line)
    counter += 1


if detergent <= 0:
    print(f"Not enough detergent, {abs(detergent)} ml. more necessary!")


