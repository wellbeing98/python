#list comprehension 을 사용해서 x 생성하기
x = []
for i in range(10):
    x.append(i+1)
print(x) #x를 생성하였고
X =[num*num for num in x]
print(X) #x*x들을 원소로 담은 집합 생성완료
