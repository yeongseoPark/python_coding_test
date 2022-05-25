# 공중 미래도시에는 1~N 의 회사가 있다. 특정 회사끼리는 도로를 통해 연결
# 방문 판매원 A는 1번회사에 위치해있으며, X번 회사에 방문해 물건을 판매하고자 한다.
# 연결된 2개의 회사는 양방향 이동이 가능, 걸리는 시간은 1
# 또한 방문 판매원 A는 기대하던 소개팅에도 참석하고자 한다.
# 소개팅 상대는 K번 회사에 존재.
# A는 X번 회사에 가서 물건을 판매하기 전, 먼저 k번 회사에 찾아가서 함께 커피를 마시 예정
# 1->k->x
# 가능한 빠르게 이동하고자 함
# 방문 판매원이 회사 사이를 이동하는 최소 시간계산

import sys 
input = sys.stdin.readline 

inf = int(1e9)

n,m = map(int,input().split())

graph = [[inf] * (n+1) for _ in range(n+1)]

for a in range(n+1):
    for b in range(n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x,k = map(int,input().split())

for _ in range(n+1):
    for a in range(n+1):
        for b in range(n+1):
            graph[a][b] = min(graph[a][b], graph[a][_] + graph[_][b])

dist = graph[1][k] + graph[k][x]

if dist >= inf:
    print(-1)

else:
    print(dist)

