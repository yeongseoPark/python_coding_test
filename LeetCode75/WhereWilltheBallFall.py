class Solution(object):
    def findBall(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        # 우하단 1
        # 좌하단 -1
        # \/ 요느낌으로 갇히거나 , 양쪽 벽에 갖다박으면 갇힘
        left = 0
        right = len(grid[0])
        bottom = len(grid)
        
        def dfs(grid, y,x):
            
            if grid[y][x] == 1: # 우하단
                if x + 1 == right: 
                    return -1
                elif grid[y][x+1] == -1:
                    return -1
                
                else:
                    if y + 1 == bottom:
                        return x+1
                    return dfs(grid, y+1, x+1) # return 없으면, 재귀의 마지막에서 값이 돌아올 수 없다
            
            
            elif grid[y][x] == -1: # 좌하단
                if x == left:
                    return -1
                elif grid[y][x-1] == 1:
                    return -1
                
                else:
                    if y + 1 == bottom:
                        return x-1
                    return dfs(grid, y+1,x-1)
        
        ans = []
        for i in range(len(grid[0])):
            ans.append(dfs(grid, 0, i))
        
        return ans

Solution().findBall([[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]])