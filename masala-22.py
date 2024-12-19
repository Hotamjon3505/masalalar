
n =int(input("nechta son kiritamiz  \n>>>"))
a=0
hatolik = 0
list = []
while a < n:
    son = int(input(">>>"))
    list.append(son)
    a += 1
for i in range(len(list)-1):
    o = int(i + 1)

    if list[i] < list[o]:
        a += 1
    else:
        print(i+1)

if a==0:
    print("0");



