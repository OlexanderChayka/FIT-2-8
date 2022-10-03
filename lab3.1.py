n= list(map(int, input('Введіть числа через пробіл ').split()))
s=0
for i in n:
    s+=sum(map(int, list(str(i))))
print(f'сумма чисел = {s}')