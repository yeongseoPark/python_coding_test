
class Solution(object):
    def climbStairs(self, n): # 재귀 사용(topdown)딕셔너리로 memo하는 방법
        """
        :type n: int
        :rtype: int
        """
        memo = {}
        memo[1] = 1
        memo[2] = 2
        
        def climb(n):
            if n in memo:
                return memo[n]
            else:
                memo[n] = climb(n-1) + climb(n-2)
                return memo[n]
        return climb(n)

    
    def climbStairs(self, n): # 재귀 사용x, dp테이블 bottom-up채우기
        """
        :type n: int
        :rtype: int
        """
        if n == 1 or n ==2: 
            return n
        
        dp = []
        dp.append(1) # dp[0] 
        dp.append(1) # dp[1]
        dp.append(2) # dp[2]
        
        for i in range(3, n+1):
            dp.append(dp[i-1]+dp[i-2])
        
        return dp[n]