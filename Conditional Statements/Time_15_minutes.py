current_hour = int(input())
current_minutes = int(input())

time_in_minutes = current_hour * 60 + current_minutes # 1 chas:20 minyti = 60 + 20. Polychawame CHASUT w minyti
time_after_15_minutes = time_in_minutes + 15 # wremeto s dobawenite 15 min SAMO w minytu

final_hour = time_after_15_minutes // 60 # obrushtame w chasowe sled dobawenite 15 min kato delim celochisleno
final_minutes = time_after_15_minutes % 60 # za da plychim ostatukut ot chasowete (95 minyti // 60 = 1
#95 % 60 = edin shas s ostatuk 35
if final_hour == 24: #prawim takawa dobawka ako imame zadaden chas ot 00:00.
    final_hour = 0  # toest ako final_hour = 24, neka stane 00

if final_minutes < 10:
    print(f'{final_hour}:0{final_minutes}')
else:
    print(f'{final_hour}:{final_minutes}')