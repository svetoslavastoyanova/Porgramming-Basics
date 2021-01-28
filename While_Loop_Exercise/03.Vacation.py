money_needed = float(input())
owned_money = float(input())
days_counter = 0
spending_counter = 0
while True:
    text = input()
    current_money = float(input())
    days_counter += 1
    if text == "save":
        owned_money += current_money
        spending_counter = 0
    elif text == "spend":
        owned_money -= current_money
        spending_counter += 1
        if owned_money < 0:
            owned_money = 0

    if spending_counter == 5:
        print(f"You can't save the money.")
        print(f"{days_counter}")
        break

    if owned_money >= money_needed:
        print(f"You saved the money for {days_counter} days.")
        break





