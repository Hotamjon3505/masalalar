a = []
n = int(input("nechta son kiritamiz \n>>>"))
i = 0
while i != n:
    i += 1
    son = int(input(">>"))
    a.append(son)
s = 1
for i in a:
    print(i**s)
    s+=1
