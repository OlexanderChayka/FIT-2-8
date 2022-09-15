print('Введіть 1 число')
print('Введіть 2 число')
while True:
    try:
        n=int(input())
        m=int(input())
        n1=0
        while n > 0 :
            n1+= n % 10
            n=n // 10
        while m > 0 :
            n1+= m % 10
            m=m // 10
        print (n1)
    except ValueError:
        print('Вы ввели не число')