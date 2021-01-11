month = input()
nights_counts = int(input())


apartment_price = 0
studio_price = 0

if month == "May" or month == "October":
    studio_price = 50 * nights_counts
    apartment_price = 65 * nights_counts

    if 7 < nights_counts < 14:
        studio_price -= studio_price * 0.05
    elif nights_counts > 14:
        studio_price -= studio_price * 0.3
        apartment_price -= apartment_price * 0.10

elif month == "June" or month == "September":
    studio_price = 75.20 * nights_counts
    apartment_price = 68.70 * nights_counts

    if nights_counts > 14:
        studio_price -= studio_price * 0.20
        apartment_price -= apartment_price * 0.10

elif month == "July" or month == "August":
    studio_price = 76 * nights_counts
    apartment_price = 77 * nights_counts

    if nights_counts > 14:
        apartment_price -= apartment_price * 0.10

print(f"Apartment: {apartment_price:.2f} lv.")
print(f"Studio: {studio_price:.2f} lv.")