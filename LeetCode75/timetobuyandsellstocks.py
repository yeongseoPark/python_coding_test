
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        left = 0
        right  = 1
        maxp = 0
        
        while right < len(prices):
            if prices[left] < prices[right]:
                maxp = max(maxp, prices[right] - prices[left])
            
            else:
                left = right 
            
            right += 1
        
        return maxp
                
        
