weidth = int(input())
length = int(input())
cake_pieces = weidth * length

while cake_pieces > 0:
    line = input()

    if line == "STOP":
        print(f"{cake_pieces} pieces are left.")
        break

    eaten_pieces = int(line)
    cake_pieces -= eaten_pieces

if cake_pieces <= 0:
    print(f"No more cake left! You need {abs(cake_pieces)} pieces more.")




