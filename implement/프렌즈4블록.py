from collections import deque

def search(graph, m,n):
    if graph[m][n] == graph[m][n+1] == graph[m+1][n] == graph[m+1][n+1] and graph[m][n] != 0: 
        #만약 기준부터 우, 우하, 하 같다면 블록이므로, 해당 칸들 리턴한다
        return [(m,n),(m,n+1),(m+1,n),(m+1,n+1)]
    
def drop(m,n,graph, deleted):
    for i in deleted: # 삭제된 셀들 0으로 바꿔주고 
        graph[i[0]][i[1]] = 0
    #땡겨주면 된다
    while True:
        moved = 0
        for i in range(m-1):
            for j in range(n):
                if graph[i][j] and graph[i+1][j]==0:
                    graph[i+1][j] = graph[i][j] 
                    # 이렇게 바꿔줘도 한번만 for문 돌아서는 맨위에 aa / 그다음에 ab(그밑에는 00)이렇게 있는경우에는
                    # 밑에것만 바뀌고 아래거는 안바뀜
                    # 그래서 더이상 밑에 0, 위에 0아닌것 있지 않을때까지 while문 돌려준다
                    graph[i][j] = 0 
                    moved = 1
        if moved == 0:
            break

def solution(m, n, board):
    board = [list(i) for i in board]
    answer = 0
    while True: 
        blocked = []
        for i in range(m-1): # 우,하를 탐색하기에 m-1,n-1까지만 포문 돌림
            for j in range(n-1):
                if search(board,i,j): # 블록인지 확인
                    blocked += search(board,i,j) #블록일경우 해당 블록들 blocked에 더함
        if blocked == []: # 만약 블록이없다면 끝냄
            break
        deleted = list(set(blocked))
        deleted.sort(key=lambda x : x[0], reverse=True)
        # 보니까 deleted까지는 맞음
        #다음번 턴이 이상함
        print(deleted)
        drop(m,n,board,deleted) 
        # blocked에 겹치는 값 있을 수 있으므로 set으로 줄여준다.
        # 
        answer += len(deleted)
        
    return answer

print(solution(4, 5, ["AAAAA","AUUUA","AUUAA","AAAAA"]))


