detergent = int(input())
detergent *= 750
counter = 1
dishes = 0
pots = 0
while detergent > 0:
    dish = input()
    if dish == "End":
        print(
            "Detergent was enough!\n{} dishes and {} pots were washed.\nLeftover detergent {} ml.".format(dishes, pots,
                                                                                                          detergent))
        exit(0)
    if counter % 3 == 0:
        detergent -= int(dish) * 15
        pots += int(dish)
    else:
        detergent -= int(dish) * 5
        dishes += int(dish)
    counter += 1

print(f"Not enough detergent, {abs(detergent)} ml. more necessary!")