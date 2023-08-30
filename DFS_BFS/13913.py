from collections import deque

n, k = map(int, input().split())

def find_path(parent, start, end):
    path = []
    cur = end
    while cur != start:
        path.append(cur)
        cur = parent[cur]
    path.append(start)
    path.reverse()
    return path

visited = [0] * 100001
parent = [-1] * 100001
q = deque()
q.append((n, 0))
visited[n] = True

while q:
    cur, cost = q.popleft()
    
    if cur == k:
        print(cost)
        for j in find_path(parent, n, k):
            print(j, end =" ")
        break
    
    for next in [cur-1, cur +1, cur *2]:
        if 0 <= next <= 100000 and not visited[next]:
            visited[next] = True
            parent[next] = cur
            q.append((next, cost + 1))
