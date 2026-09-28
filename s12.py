n = int(input("Введите число N: "))
k = 0 #счётчик шагов
print(n,end=" ")
while n!=1:
    if n%2==0:
        n = n//2
    else:
        n = n*3+1
    print(n, end=" ")
    k +=1
print("/Общее кол-во шагов:", k)