from itertools import combinations


n, m = map(int,input().split())

nums = list(map(int,input().split()))

cases = list(combinations(nums,3))

meet_condition = []
for case in cases:
    if sum(case) <= m:
        meet_condition.append(case)

answer= 0 
for i in meet_condition:
    answer = max(answer, sum(i))

print(answer)

