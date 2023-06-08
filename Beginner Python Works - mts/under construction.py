
d = None
m = int(input("enter first number (between 1 and 100):"))
n = int(input("enter second number ( between 1 and 100):"))

      
for i in range(1, 100):
    if (m % i == 0) and (n % i == 0):
        d = i
    else:
        continue
print(d)
        