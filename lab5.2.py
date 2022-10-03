import math
A=float(input("введіть перше число: "))
B=float(input("введіть друге число: "))
C=float(input("введіть третє число: "))
O=0.0
if B>A and C>A:
   print('Найменше А')
elif B>C and A>C:
   print('Найменше С')
if C>B and A>B: 
   print('Найменше В')