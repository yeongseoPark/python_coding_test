# 시험을 본 학생 N명의 성적을 분실한 선생님. 
# 성적을 비교한 결과의 일부만 가지고 있음
# 학생 N명의 성적은 모두 다름
# 학생들의 성적을 비교한 결과가 주어질 때, 성적 순위를 정확히 알 수 있는 학생은 모두 몇명인지 계산
import sys
input = sys.stdin.readline
inf = int(1e9)

n,m = map(int, input().split())

graph = [[inf] * (n+1) for _ in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    graph[a][b] = 1

for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            graph[i][j] = 0

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1): 
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])


# a->b OR b->a가 가능할 시, 성적 비교가 가능한 것. 
result = 0
for i in range(1,n+1):
    count = 0 # 각 학생을 한명씩 확인하며 도달 가능한지 체크 # 만약 어떤 학생이 나머지 학생에 대해 도달가능(비교가능)하다면 순위를 정확히 알 수 있는 것
    for j in range(1,n+1): 
        if graph[i][j] != inf or graph[j][i] != inf:
            count += 1
    if count == n:
        result += 1


print(result)




