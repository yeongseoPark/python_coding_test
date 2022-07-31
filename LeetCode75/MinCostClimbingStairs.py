class Solution(object):
    def minCostClimbingStairs(self, cost): # bottom-up
        """
        :type cost: List[int]
        :rtype: int
        """
        # top = len(cost)
        
        dp = []
        dp.append(cost[0])
        dp.append(cost[1])
        
        for i in range(2 , len(cost)+1):
            if i != len(cost):
                dp.append(min(dp[i-1], dp[i-2]) + cost[i])
            else:
                dp.append(min(dp[i-1], dp[i-2]))
        
        return dp[len(cost)]

class Solution(object):
    def minCostClimbingStairs(self, cost): # top-down memoization
        """
        :type cost: List[int]
        :rtype: int
        """
        # top = len(cost)
    
        n = len(cost)
        dp   = [0] * n
        
        def MinCost(cost, n):
            if n == 0 or n == 1: # base case
                return cost[n]
            elif dp[n] != 0:
                return dp[n]
            
            dp[n] = cost[n] + min(MinCost(cost, n-1), MinCost(cost,n-2))
            
            return dp[n]
        
        return min(MinCost(cost, n-1), MinCost(cost, n-2))