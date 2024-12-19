

a = [1,2,5,0,5,2,3,4,0,6,53,3,9,0]
boshlash = 0
ohiri = 0

for i in range(len(a)):
    if a[i] == 0 :
        if boshlash==0:
            boshlash = i
        else:
            if ohiri==0:
                ohiri = i

yigndi = 0

for j in range(boshlash,ohiri):
    yigndi += a[j]
print(yigndi)