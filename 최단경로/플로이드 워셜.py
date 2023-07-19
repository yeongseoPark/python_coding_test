inf = int(1e9)

n = int(input())
m = int(input())

graph = [[inf] * (n+1) for _ in range(n+1)] # 2차원 리스트 

for a in range(1,n+1):
    for b in range(1,n+1):
        if a == b:
            graph[a][b] = 0 # 자기에서 자기로 가는 경우 0 으로 초기화 

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a][b] = c # a -> b 비용은 c

# 점화식 Dab = min(Dab , Dak+Dkb)에 따라 알고리즘 수행 
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b]) 

for a in range(1,n+1): # 출력
    for b in range(1, n+1):

        if graph[a][b] == inf:
            print("infinity", end=" ")
        
        else:
            print(graph[a][b], end = " ")
    print()