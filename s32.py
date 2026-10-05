import math
N = int(input("Введите число N: "))
limit = int(math.sqrt(N)) + 1 #найти макс знач для перебора
for a in range(limit):
    if a * a > N:
        continue
    for b in range(a, limit):
        if a * a + b * b > N:
            continue
        for c in range(b, limit):
            if a * a + b * b + c * c == N:
                print(a, b, c)