import math
year = input()
holidays_p = int(input())
weekends_h = int(input())
weekends_sofia = (48 - weekends_h)*3/4
holidays = holidays_p*(2/3)
total_games = weekends_sofia + holidays + weekends_h
more_games = 0
if year == "normal":
    print(math.floor(total_games))
elif year == "leap":
    more_games = total_games + (total_games * 0.15)
    print(math.floor(more_games))




