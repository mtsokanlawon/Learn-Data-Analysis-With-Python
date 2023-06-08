m = int(input("enter first number:"))
n = int(input("enter second number"))
if m>n:
    d=n
else:
    d=m
while ((m % d != 0) or (n % d != 0)) and (d!=1):
    d-=1
if d==1:
    print ("It has no gcd")
else:
    print (d)
    