a =[3,4,5,2,6,3,7]
s = 0
m=[1,2,3,4,5]
for i in m:
    if a[i]>a[i+1] and a[i-1]<a[i] or a[i]<a[i+1] and a[i-1]>a[i]:
        s+=1
    else:
        print(f"buzg'unchi eliment >> {i}")

print(0)