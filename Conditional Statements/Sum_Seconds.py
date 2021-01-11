time_first = int(input())
time_second = int(input())
time_third = int(input())

total_time = time_first + time_second + time_third

minutes = total_time // 60
seconds = total_time % 60
#minutes.math.floor(minutes) - ako pishem edna "/" predi delenieto s 60,za da zakruglim nadoly

if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')
#След като сте намерили сбора от секундите трябва да ги превърнете в минути и секунди (например,
ако сборът е 85 секунди това са 1 минута и 25 секунди, защото 1 минута има 60 секунди). Създайте
две нови променливи. В първата изчислете колко минути е сборът от секунди като разделите сбора
на 60. Във втората променлива изчислете секундите с помощта на деление с остатък (%), за да
вземете остатъка при деление с 60. Например имате общ сбор от 134 секунди (2 минути и 14 секунди)
след целочисленото деление (//) на 60 ще получим 2, а след делението с остатък (%) ще получим
оставащите секунди(14)