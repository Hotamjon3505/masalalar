import math
n = int(input("n ni kiriting \n>>>"))
a =[]
for i in range(n):
    a.append(int(input(">>")))
for j in a:
    if n != 0:
        k = math.pow(j, n)
        print(k)
    n -=1

