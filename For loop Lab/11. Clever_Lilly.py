age = int(input())
laundry_price = float(input())
toy_price = int(input())

all_toys = 0
money = 0
given_money = 10


for current_age in range(1, age + 1):
    if current_age % 2 == 1:
        all_toys += 1

    else:
        money += given_money - 1
        given_money += 10

money += all_toys * toy_price

if money >= laundry_price:
    left = money - laundry_price
    print(f"Yes! {left:.2f}")
else:
    money_needed = laundry_price - money
    print(f"No! {money_needed:.2f}")