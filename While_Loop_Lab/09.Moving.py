width = int(input())
length = int(input())
height = int(input())
place_size = width * length * height



while place_size > 0:
    line = input()
    if line == "Done":
        print(f"{place_size} Cubic meters left.")
        break
    boxes = int(line)
    place_size -= boxes

if place_size <= 0:
    print(f'No more free space! You need {abs(place_size)} Cubic meters more.')


