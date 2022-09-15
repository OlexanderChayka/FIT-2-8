print('Введіть довжину ребра')
while True:
    try:
        length=float(input())
        S=length**2*4
        print ('Площа куба = ', str(S))
        V=length**3
        print ("Об'єм куба = ", str(V))
    except ValueError:
        print('Вы ввели не число')