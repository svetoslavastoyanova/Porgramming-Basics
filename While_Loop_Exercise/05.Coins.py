change = float(input())
coin_counts = 0

while change != 0:
    if change >= 2:
        change -= 2
        coin_counts += 1
    elif change >= 1:
        change -= 1
        coin_counts += 1
    elif change >= 0.50:
        change -= 0.50
        coin_counts += 1
    elif change >= 0.20:
        change -= 0.20
        coin_counts += 1
    elif change >= 0.10:
        change -= 0.10
        coin_counts += 1
    elif change >= 0.05:
        change -= 0.05
        coin_counts += 1
    elif change >= 0.02:
        change -= 0.02
        coin_counts += 1
    elif change >= 0.01:
        change -= 0.01
        coin_counts += 1
else:
    print(coin_counts)