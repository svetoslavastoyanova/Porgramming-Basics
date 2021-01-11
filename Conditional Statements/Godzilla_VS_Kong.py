budget = float(input())
actor_counts = int(input())
clothes = float(input())

decor = 0.1*budget
clothes_total_price = actor_counts*clothes

if actor_counts > 150:
    clothes_total_price -= 0.1*clothes_total_price # clothes_total_price = 0.9*clothes_total_price

money_needed = clothes_total_price + decor

if money_needed > budget:
    print('Not enough money!')
    print(f' Wingard needs {(money_needed - budget):.2f} leva more.')
#nedostigashtite parı, namırame kato ot parite koito ni trqbwat wadim budget s koito razpolagame
# mojem da izwurshim delenieto naprawo w skobite s dopulnitelni () predi {}
else:
    print('Action!')
    print(f'Wingard starts filming with {(budget - money_needed):.2f} leva left.')

# ostawashtite pari, namirame, kato ot budget ( skoito razpolagame) izwadim parite, koito shte ni trqbwat.


