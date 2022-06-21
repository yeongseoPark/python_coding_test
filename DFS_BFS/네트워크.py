def solution(n, computers): #답보고품
    answer = 0
    visited = [False for i in range(n)]
    for com in range(n):
        if visited[com] == False:
            DFS(n, computers, com, visited)
            answer += 1 #DFS로 최대한 컴퓨터들을 방문하고 빠져나오게 되면 그것이 하나의 네트워크.
    return answer

def DFS(n, computers, com, visited):
    visited[com] = True
    for connect in range(n):
        if connect != com and computers[com][connect] == 1:
            #connect가 com(탐색시작하는 노드)아니고 
            #연결된 컴퓨터
            if visited[connect] == False:
                DFS(n, computers, connect, visited)
