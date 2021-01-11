import math
record_in_seconds = float(input())
distance_in_meters = float(input())
seconds_per_meter = float(input())

total_seconds = distance_in_meters*seconds_per_meter #izchislqwame obshtiqt broi na sekyndite za wsichki metri
delay_counts = math.floor(distance_in_meters)/15 # ili distance_in_meters// 15 * 12.5
# izchislqwame kolko puti shte se zabawi kato delim obshto metrite na wseki 15 metra
extra_seconds = math.floor(delay_counts)*12.5 #izchislqwame dopulnitelnite sekyndi: broi puti na zabawqne po 12.5 sekyndi
result = total_seconds + extra_seconds # dobawqme dopulnitelnite sekyndi kum obshtite

if result < record_in_seconds:
    print(f' Yes, he succeeded! The new world record is {result:.2f} seconds.')
else:
    print(f'No, he failed! He was {(result - record_in_seconds):.2f} seconds slower.')

# drygo reshenie: total_seconds = distance_in_meters * seconds_per_meter
#delay_counts = distance_in_meters // 15 * 12.5   // - celochisleno delenie
#total_seconds += delay_counts