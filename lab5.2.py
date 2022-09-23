import math

A=float(input("Введіть перше число:  "))
B=float(input("Введіть друге число:  "))
C=float(input("Введіть третє число:  "))

O=0.0

if B>A and C>A:
   print('Найменше А')
elif B>C and A>C:
   print('Найменше B')
elif C>B and A>B: 
   print('Найменше C')