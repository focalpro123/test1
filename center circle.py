import math
def rad(x,y,h,k):
    return math.sqrt((x-h)(x-h)-(y-k)(y-k))
x=float(input("Enter point x on circle"))
y=float(input("nter pt y on circle"))
h=float(input("Enter h on centre"))
k=float(input("nter k on centre"))
A=3.14*rad(x,y,h,k)*rad(x,y,h,k)
print(A)


















