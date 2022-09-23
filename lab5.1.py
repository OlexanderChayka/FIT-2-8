import math

x=float(input("Введіть число х:  "))

def func1(x1):
   rez=7*math.log1p(x1)+math.log(x1,7)+math.log10(x1)
   return(rez)
def func2(x2):
   rez=math.sin(x2)-math.cos(x2+2+math.pi/7)
   return(rez)
def func3(x3):
   rez=2.24*math.e**(0.5*x3+0.1)*2**(0.3*x3)
   return(rez)
y=0.0
if x >= 1.0:
    y=func1(x)
elif -10.3 < x < 1.0:
    y=func2(x)
elif x <= -10.3:
    y=func3(x)

print(y)