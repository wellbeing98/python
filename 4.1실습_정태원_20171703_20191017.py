#sort 사용한 경우
a = [8, 4, 9, 5]
a.sort()
print(a[0])
#sort를 사용하지 않은 경우
a = [8, 4, 9, 5]
min = a[0]
for i in range(0,len(a)-1):
    if min > a[i]:
        min = a[i]
print(min)   
