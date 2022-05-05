# n*m 크기의 얼음 틀
# 세로 n , 가로 m
# 구멍 뚫려있는 부분은 0, 칸막이 존재 부분 1
# 생성되는 총 아이스크림의 개수

n,m = map(int,input().split())

graph = [] #0혹은1의 정수 리스트
for i in range(n):
    graph.append(list(map(int,input().split())))

def dfs(x,y):
    if x<=-1 or x>= n or y<=-1 or y>=m: # 주어진 범위를 벗어나는 경우 즉시 종료
        return False 

    # 현재 노드가 아직 방문하지 않은 노드, 구멍 뚫려있다면
    if graph[x][y] == 0:
        #해당 노드 방문처리(구멍 막아버림)
        graph[x][y] = 1
        # 상,하,좌,우 위치도 재귀적으로 모두 호출해서 구멍 막음
        dfs(x-1,y)
        dfs(x,y-1) # 연결된 모든 노드에 대해방문 처리만 하는 목적(1로바꾸기)
        dfs(x+1,y)
        dfs(x,y+1)
        return True # 시작점 노드 true값 반환
    return False # graph[x][y]값이 1이라면(방문했다면) False출력


result = 0 
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i,j) == True: # dfs 수행 결과가 true(처음 방문하면서 구멍임, 주변 구멍 다 막음)
            result += 1 # 카운트를 늘려줌
    
print(result)
