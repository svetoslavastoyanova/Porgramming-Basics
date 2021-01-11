number = float(input())
convert_from = input()
convert_to = input()

number_in_meters = 0
if convert_from == "mm":
    number_in_meters = number / 1000 # delim na 1000, za da prewurnem w milimetri
elif convert_from == "cm":
    number_in_meters = number/100 #delim na 100, za da prewurnem w cm
else:
    number_in_meters = number

result = 0
if convert_to == "mm":
    result = number_in_meters*1000 # ymnojawame po 1000, za da prewurnem w metri
elif convert_to == "cm":
    result = number_in_meters*100 # ymnijawame po 100, za da prewurnem w cm
else:
    result = number_in_meters

print(f"{result:.3f}")