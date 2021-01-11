import math
leva_income = float(input())
average_success = float(input())
minimal_salary = float(input())

social_scholarship = math.floor(minimal_salary)*0.35
excellence_scholarship = math.floor(average_success) * 0.25


if leva_income < minimal_salary and average_success > 4.5:
    print(f"You get a Social scholarship {math.floor(social_scholarship)} BGN")
elif average_success > 5.5:
    print(f'You get a scholarship for excellent results math.floor{math.floor(excellence_scholarship)} BGN')
else:
    print(f'You cannot get a scholarship!')

