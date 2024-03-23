n=5752
s=0
n1=n
while n>0:
    d=n%10
    s=s+d
    n=n//10
if n1%s==0:
    print("divisible")
else:
    print("not divisible")
