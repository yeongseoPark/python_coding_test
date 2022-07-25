class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """ 
        visited = [[False] * len(image[0]) for _ in range(len(image))]
        
        starting = image[sr][sc]
                
        self.dfs(sr,sc, visited, image, color , starting)
        
        return image
                
    def dfs(self, x, y, visited, image, color, starting):
        dx = [0, 0, 1 , -1] # 동 서 남 북
        dy = [1, -1, 0 , 0]

        if (not visited[x][y]) and (image[x][y] == starting):
            visited[x][y] = True
            image[x][y]   = color
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < len(image) and 0 <= ny < len(image[0]):
                    self.dfs(nx,ny,visited, image,color, starting)
                     # 여기 return을 달아줘서 계속 [[1,1,1],[1,2,0],[1,0,1]] 이런 결과가 나옴
                    # 이는 14줄에서 호출한 dfs의 값을 dfs(1, 2, visited ,image, color ,starting)의 결과로 한다는 뜻
                    # 근데 1, 2는 22 라인의 조건에 만족하지 못하므로, 바로 그냥 함수가 끝나버림
                    # 그래서 재귀가 이어지지 못함
                    # dfs를 만든 의도는 같은 값을 타고가면서 색을 바꾸게 하려 한 것인데, 이 return 때문에 재귀적으로 수행이 안되고 중간에 끝나게 됨
                    # return을 빼줌으로써 의도대로 재귀가 끝까지 이어지고 자동으로 함수가 끝나게 함(함수는 for문을 다 돌고 알아서 종료)
        
    # visited 없이 푼 방법
    class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """ 
        def dfs(i, j):
            image[i][j] = color # 새 색으로 칠해줌
            for x,y in ((i-1,j), (i+1,j), (i,j-1),(i,j+1)): # 동서남북을 튜플로 표현
                if 0 <= x < m and 0 <= y < n and image[x][y] == old : # 지도를 벗어나지 않았으면
                    dfs(x,y)
            
        old = image[sr][sc] # 기존 색깔(현재칸)
        m,n = len(image), len(image[0])

        if old != color: # 현재칸 색깔과 바꾸려는 색깔이 다르면 dfs 
            dfs(sr,sc)
        
        return image
                    
        
