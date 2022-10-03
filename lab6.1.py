import math
import numpy as np
a=float(input("Введіть діапазон (а):  "))
b=float(input("Введіть діапазон (b):  "))
h=float(input("Введіть крок (h)  "))
for x in np.arange(a,b+h,h):
   y=(x**3+1*math.fabs(x))/3**x
   print("x=%.1f   y=%.3f"%(x,y))