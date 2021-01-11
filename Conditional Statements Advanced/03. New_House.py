flowers = input()
flowers_count = int(input())
budget = int(input())

price = 0

if flowers == "Roses":
    price = flowers_count*5
    if flowers_count > 80:
        price -= price * 0.10
elif flowers == "Dahlias":
    price = flowers_count * 3.80
    if flowers_count > 90:
        price -= price * 0.15
elif flowers == "Tulips":
    price = flowers_count * 2.80
    if flowers_count > 80:
        price -= price * 0.15
elif flowers == "Narcissus":
    price = flowers_count * 3
    if flowers_count < 120:
        price += price * 0.15
elif flowers == "Gladiolus":
    price = flowers_count * 2.50
    if flowers_count < 80:
        price += price * 0.20
if budget >= price:
    print(f"Hey, you have a great garden with {flowers_count} {flowers} and {budget - price:.2f} leva left.")
else:
    print(f"Not enough money, you need {price - budget:.2f} leva more.")