budget = int(input())
season = input()
fishers_count = int(input())

rent_price = 0
if season == "Spring":
    rent_price = 3000
elif season == "Summer" or season == "Autumn":
    rent_price = 4200
elif season == "Winter":
    rent_price = 2600

if fishers_count <= 6:
    rent_price -= rent_price * 0.10
elif 7 <= fishers_count <= 11:
    rent_price -= rent_price * 0.15
elif fishers_count > 12:
    rent_price -= rent_price * 0.25

if fishers_count % 2 == 0 and season != "Autumn":  # ili not season == "Autumn"
    rent_price -= rent_price * 0.05
# moje da suzdadem promenliwa "diff"diff = abs(budget - rent_price) abs shte izkara cqlo chislo, ako rezyltatut e bil
# otricatelen. posle wpiswame naprawo diff doly za symata {diff:.2f)
if budget >= rent_price:
    print(f"Yes! You have {budget - rent_price:.2f} leva left.")
elif budget < rent_price:
    print(f"Not enough money! You need {rent_price - budget:.2f} leva.")

