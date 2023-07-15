from collections import deque

number = int(input())
linked = int(input())

mapping = [[] for _ in range(number + 1)]
for _ in range(linked):
    a ,b = map(int, input().split())
    mapping[a].append(b)
    mapping[b].append(a)

cnt = 0
q = deque([1])
visited = [False] * (number + 1)
visited[1] = True  # 시작 노드를 방문 표시

while q:
    tmp = q.popleft()  # popleft를 사용해 BFS를 구현

    for i in mapping[tmp]:
        if not visited[i]:
            visited[i] = True
            cnt += 1
            q.append(i)

print(cnt)
