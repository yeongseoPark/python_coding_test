n = int(input())
k = int(input())

if n < k :
    print(0)
    exit()

seq = list(map(int, input().split()))
seq.sort()

dist = []
for i in range(len(seq) - 1):
    dist.append(seq[i+1] - seq[i])

dist.sort()
print(sum(dist[:-(k-1)])) 
# 가장 긴 k-1개의 거리들을 그룹으로 분할하는 점으로 사용