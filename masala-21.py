
n =int(input("nechta son kiritamiz  \n>>>"))
a=0
list = []
while a < n:
    son = int(input(">>>"))
    list.append(son)
    a += 1
for i in range(len(list)-1):
    o = int(i + 1)

    if list[i] > list[o]:
        print("hato");
    else:
        print("tug'ri")


