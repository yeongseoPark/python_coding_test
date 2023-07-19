# https://www.acmicpc.net/problem/11404

import sys
input = sys.stdin.readline
inf = int(1e9)

n = int(input()) # 도시의 개수 n
m = int(input()) # 버스의 개수 m

graph = [[inf] * (n+1) for _ in range(n+1)] 

for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b] = 0

for i in range(m):
    a, b, c= map(int,input().split())
    graph[a][b] = min(graph[a][b],c) # 도시 사이 간선이 여러개일 수 있다했으니, 가장 짧은 간선 정보만 저장

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == inf:
            print(0, end=" ")
        else:
            print(graph[i][j], end=" ")
    print()

