import sys
n = int(input())
OddMin = sys.maxsize
OddMax = - sys.maxsize
EvenMin = sys.maxsize
EvenMax = - sys.maxsize
OddSum = 0
EvenSum = 0

for i in range(1, n + 1):
    number = float(input())

    if i % 2 == 0: # tyk smqtame s index, a s number,kakto w minalata zadacha, zashtoto izchislqwame poziciite
        EvenSum += number

        if EvenMax < number:
            EvenMax = number

        if EvenMin > number:
            EvenMin = number
    else:
        OddSum += number

        if OddMax < number:
            OddMax = number

        if OddMin > number:
            OddMin = number


print(f"OddSum={OddSum:.2f},")
if OddMin == sys.maxsize:
    print(f"OddMin=No,")
else:
    print(f"OddMin={OddMin:.2f},")
if OddMax == - sys.maxsize:
    print(f"OddMax=No,")
else:
    print(f"OddMax={OddMax:.2f},")
print(f"EvenSum={EvenSum:.2f},")
if EvenMin == sys.maxsize:
    print(f"EvenMin=No,")
else:
    print(f"EvenMin={EvenMin:.2f},")
if EvenMax == - sys.maxsize:
    print("EvenMax=No")
else:
    print(f"EvenMax={EvenMax:.2f}")