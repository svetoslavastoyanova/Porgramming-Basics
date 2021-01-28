account = 0

while True:
    line = input()
    if line == "NoMoreMoney":
        break
    money = float(line)
    if money < 0:
        print("Invalid operation!")
        break
    account += money
    print(f"Increase: {money:.2f}")

print(f"Total: {account:.2f}")