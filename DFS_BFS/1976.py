# 같은 도시 여러번 방문 가능 - BFS로 하면 끝나지 않음
# 방문 도시들을 포함하는 연결된 그래프가 있는가를 판단하면 됨?
# 그냥 방문 도시중 하나에서 DFS해서 여행지들이 모두 포함됐는지 확인하면 될것 같은데

from collections import defaultdict

n = int(input())
m = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

destinations = list(map(int, input().split()))
if len(destinations) == 0:
    print("NO")
    exit()
    
dest_dic = dict()

for dest in destinations:
    dest_dic[dest-1] = 0

destinations_set = set(list(x - 1 for x in destinations))

visited = [0] * n
def dfs(cur, depth):
    if depth == n:
        return 

    visited[cur] = True
    if cur in destinations_set:
        dest_dic[cur] = 1
    
    for i in range(len(graph[cur])):
        if graph[cur][i] == 1:
            if not visited[i]:
                dfs(i, depth + 1)

dfs(destinations[0]- 1, 0)

if len(set(dest_dic.values())) == 1 and list(dest_dic.values())[0] == 1:
    print("YES")

else:
    print("NO")