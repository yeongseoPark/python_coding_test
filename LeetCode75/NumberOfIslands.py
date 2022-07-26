# https://leetcode.com/problems/number-of-islands/

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        def dfs(x, y):
            dx = [0, 0, -1, 1] # 동 서 남 북
            dy = [1, -1, 0, 0]
            
            if grid[x][y] == "1" and  not visited[x][y]:
                visited[x][y] = True
                
                for i in range(4):
                    nx =x + dx[i]
                    ny =y + dy[i]
                    
                    if 0<=nx<m and 0<=ny<n:
                        dfs(nx,ny)

        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]
        
        cnt = 0
        
        for i in range(m):
            for j in range(n):
                if (not visited[i][j]) and grid[i][j] == "1":
                    dfs(i,j)
                    cnt += 1
        
        return cnt

    # visited 없이 푸는 법
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        def sink(i, j):
            dx = [0, 0, -1, 1] # 동 서 남 북
            dy = [1, -1, 0, 0]
            
            if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == "1":
                grid[i][j] = "0" # 범위 안이고, 육지면 가라앉혀버림
                
                for k in range(4): # 동서남북도 재귀적으로 탐색해서 가라앉히는 과정 반복
                    sink(i + dx[k], j + dy[k])
                return 1 # sink한 곳이 육지여서, 하나의 섬 다 가라앉히고 1 리턴 
                # 섬 하나당 1씩 리턴하는 꼴
            
            return 0 # sink한 곳이 바다면 0 리턴
        
        summ = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                summ += sink(i,j) # 섬하나당 1이니까 그 값 더해줌
        
        return summ
            
                    
        
            
            
            