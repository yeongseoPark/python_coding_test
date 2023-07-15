n , m = map(int ,input().split())

mapping = [list(input().rstrip()) for _ in range(m)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def dfs(i, j, flag):
    global w_score, b_score

    # 점수 증가
    if flag == 'W':
        w_score += 1
    elif flag == "B":
        b_score += 1

    visited[i][j] = True
    for c in range(4):
        newx = j + dx[c]
        newy = i + dy[c]

        if 0 <= newx < n and 0 <= newy < m and not visited[newy][newx] and mapping[newy][newx] == flag:
            dfs(newy, newx, flag)


visited = [[0] * n for _ in range(m)]
b_score_total = 0
w_score_total = 0
for i in range(m): # 세로 
    for j in range(n): # 가로
        if not visited[i][j]:
            if mapping[i][j] == "W":
                w_score = 0
                dfs(i, j, 'W')
                w_score_total += w_score * w_score  # 여기서 총 점수를 계산
            else:
                b_score = 0
                dfs(i, j, 'B')
                b_score_total += b_score * b_score  # 여기서 총 점수를 계산

print( w_score_total, b_score_total)  # 총 점수 출력