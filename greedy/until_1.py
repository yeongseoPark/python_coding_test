# N이 1이 될때까지 
# 1. n-1 / 2. n/k => 반복적으로 수행
# 단 n/k는 나눠떨어질때만 가능
# n과 k가 주어질 때 n이 1될때까지 1번 혹은 2번 과정 수행해야 하는 최소 횟수

n, k = map(int,input().split())

# 1
# count = 0 # while문 안에 있을 시 매번 초기화됨
# while True:   
#     if n%k==0:
#         n = n/k
#         count += 1
#         if n == 1:
#             print(count)
#             break
#     else:
#         n -= 1
#         count += 1
#         if n == 1:
#             print(count)
#             break

# 2 
# count = 0 
# while n >=k: # n>=k일때는 나누는게 무조건 이득
#     while n % k != 0: #안나눠지면,나눠질때까지 빼주기
#         n -= 1
#         count += 1
#     n //= k
#     count += 1

# while n>1: # n이 k보다 작아졌을때, 1이 될때까지
#     n -= 1
#     count += 1

# print(count)

# 3 n이 k배수 되도록 한번에 빼는 방법(2번처럼 일일이x)
count = 0 
while True:
    target = (n//k)*k #k로 나눠지는 숫자가 타겟
    count += n-target #n이 target될때까지 1로빼줌(그 횟수)
    n = target

    if n<k:
        break
    count += 1
    n //= k

count += n-1 # k보다 작아진 n 1로만들기 위해 빼주는 횟수
print(count)