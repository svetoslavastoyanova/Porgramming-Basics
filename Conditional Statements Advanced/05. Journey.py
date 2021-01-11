budget = float(input())
season = input()

destination = ""
place_type = ""
price = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        place_type = "Camp"
        price = budget * 0.30
    else:
        place_type = "Hotel"
        price = budget * 0.70

elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        place_type = "Camp"
        price = budget * 0.40
    else:
        place_type = "Hotel"
        price = budget * 0.80

else:
    destination = "Europe"
    place_type = "Hotel"
    price = budget * 0.90

print(f"Somewhere in {destination}")
print(f"{place_type} - {price:.2f}")