x=int(input("Enter Number to Check Armstrong or not: "))
s=0
d=0
copy=x
while(x>0):
    d=x%10
    s=s+d**3
    x=x//10
if(s==copy):
    print("ARM")
else:
    print("Not")
