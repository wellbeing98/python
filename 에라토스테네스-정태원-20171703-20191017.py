#에라토스테네스의 체
import math
N = int(input("N을 지정하십시요" ))
list_N = list()
for i in range(1, N+1):
    list_N.append(i)
print("N까지 의 수를 출력해보겠습니다.",list_N)

n = int(math.sqrt(N))#n까지의 소수들을 구해내면 그 소수의 배수들로만 지워내도 충분
#n까지 소수 구하기
list_n = []
for i in range(1, n+1):
    list_n.append(i)
print("n까지 의 수를 출력해보겠습니다.",list_n)

        
for i in range(2,n+1):   
    for j in range(2,i): #i보다 작은수로 나누어 보기 2는 2보다 작은수가 1밖에 없음
        if i!=j and i%j == 0:
            list_n.remove(i)
            break
list_n.remove(1)
print("n까지의 소수는 ",list_n)
#list_n의 수로 N 의 소수의외의 수를 제거하기
for k in list_N:
    for p in list_n:
        if k > p and k%p == 0:
            list_N.remove(k)
            break
list_N.remove(1)#1은 따로 제거해줌

print(list_N)#완성

        
            
        
