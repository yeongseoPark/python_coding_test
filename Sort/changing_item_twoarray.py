# 배열 A와 B
# 둘 다 N개의 원소로 구성됨(1<=n<=100000), (0<=k<=n)
# 원소는 모두 자연수
# k번의 바꿔치기 연산: a배열과 b배열의 원소 하나씩 골라서 둘이 바꾸는 것
# 목표는 a배열 모든 원소의 합이 최대가 되도록 하는 것

n, k = map(int,input().split())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort() # 오름차순
b.sort(reverse=True) # 내림차순

for i in range(k): # k번만큼
    if a[i] < b[i]: # a의 원소가 b의 원소보다 작은 경우
        # 오름차순 vs 내림차순이기에 a에서 작은것부터, b에서 큰것부터 비교하게 됨
        a[i],b[i] = b[i],a[i] # 두 원소 교체
    else:
        break # a원소가 b원소보다 크거나 같은 경우 더이상 확인할필요 x

print(sum(a))



#첫 풀이: append와 remove활용, a의 최솟값이 b의 최댓값보다 큰 경우 고려하지 않음
# for i in range(k):
#     minest_a = min(a)
#     maxest_b = max(b)
#     a.append(maxest_b)
#     a.remove(minest_a)
#     b.append(minest_a)
#     b.remove(maxest_b)
# print(sum(a))