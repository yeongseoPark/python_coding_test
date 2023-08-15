from collections import deque
n, k = map(int, input().split())
visited = [-1] * 100001
q = deque()
q.append(n)
visited[n] = 0

while q:
    tmp = q.popleft()

    if tmp == k:
        print(visited[tmp])
        break

    if 0 <= tmp-1 <= 100000 and visited[tmp-1] == -1 :
        visited[tmp-1] = visited[tmp] + 1
        q.append(tmp-1)
        

    if 0 <= tmp * 2 <= 100000 and visited[tmp*2] == -1:
        q.appendleft(tmp*2)
        visited[tmp*2] = visited[tmp]

    if 0 <= tmp +1 <= 100000 and visited[tmp+1] == -1:
        visited[tmp+1] = visited[tmp] + 1
        q.append(tmp+1)
