from collections import deque

s = int(input())

q = deque() # 현재 이모티콘 개수, 클립보드에 있는 개수
q.append((1,0))

# 방문 표시 : (현재 이모티콘 개수, 클립보드 이모티콘 개수)가 키값인 딕셔너리
visited = dict() 
visited[(1,0)] = 0

while q:
    now , clip = q.popleft() # 이모티콘 개수, 클립보드에 있는 개수

    # bfs를 통해 s초에 최단으로 도달
    if now == s:
        print(visited[(now, clip)])
        break 
    
    # 화면에 있는 이모티콘 모두 복사해서 클립보드에 넣기
    if (now, now) not in visited.keys():
        visited[(now, now)] = visited[(now, clip)] + 1 # 모든 연산에 1초씩 걸리니까 다 + 1 
        q.append((now, now))
    
    # 클립보드에 있는 모든 이모티콘 화면에 붙여넣기
    if (now + clip, clip) not in visited.keys():
        visited[(now + clip, clip)] = visited[(now, clip)] + 1
        q.append((now + clip, clip))
    
    # 화면에 있는 이모티콘 중 하나 삭제하기
    if (now - 1, clip) not in visited.keys():
        visited[(now - 1, clip)] = visited[(now, clip)] + 1
        q.append((now - 1, clip))