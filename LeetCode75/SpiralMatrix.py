# https://leetcode.com/problems/spiral-matrix/discuss/394774/python-3-solution-for-spiral-matrix-one-of-the-most-easiest-you-will-never-forget

class Solution(object): # 답봤음..
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """        
        height = len(matrix)
        width = len(matrix[0])
        
        top = 0
        bottom = height - 1
        left = 0
        right = width - 1
        
        ans = []
        
        while top < bottom and left < right:
            for col in range(left, right): # →
                ans.append(matrix[top][col])
                
            for row in range(top, bottom): # ↓
                ans.append(matrix[row][right]) 
            
            for col in range(right, left, -1):
                ans.append(matrix[bottom][col]) # ←
            
            for row in range(bottom, top , -1): # ↑
                ans.append(matrix[row][left])
            
            top += 1
            bottom -= 1
            left += 1
            right -= 1
        
        if len(ans) < height*width: # 안에 남은 1Xn 혹은 MX1 처리
            for row in range(top, bottom + 1):
                for col in range(left, right + 1):
                    ans.append(matrix[row][col])
        
        return ans