# https://www.acmicpc.net/problem/10819
from itertools import permutations

n = int(input())

a = list(map(int,input().split()))

cases = list(permutations(a)) # 순열을이용해 모든 경우의 수 고려 

answer = 0 
for case in cases:
    summed = 0
    for i in range(n-1):
        summed += abs(case[i]-case[i+1])
    
    answer = max(answer, summed)

print(answer)