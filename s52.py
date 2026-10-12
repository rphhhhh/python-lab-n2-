N = int(input())
prod = 1
min_dig = 1
min_in = 1
cur_in = 1
while N > 0:
    cur_in += 1
    dig = N % 10
    if dig % 2 != 0:
        prod *= dig
        if dig < min_dig:
            min_dig = dig
            min_in = cur_in
        N = N // 10
print("Произведение нечет цифр:", prod)
print("Мин цифра:", min_dig)
print("Порядковый номер мин справа:", min_in)
