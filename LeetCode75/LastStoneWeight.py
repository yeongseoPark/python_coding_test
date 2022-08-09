class Solution(object): 
    def lastStoneWeight(self, stones): #O(n^2)
        """
        :type stones: List[int]
        :rtype: int
        """
        stones.sort()
        
        
        while len(stones) > 1:
            first  = stones.pop() 
            second = stones.pop()
            
            if first == second:
                pass            
            elif first > second:
                stones.append(first-second)
                stones.sort()
        
        if stones:
            return stones[-1] 
        else:
            return 0
        

from heapq import heappop, heappush,heapify

class Solution(object):
    def lastStoneWeight(self, stones): # 최대 heap 사용, O(N log N)
        """
        :type stones: List[int]
        :rtype: int
        """
        for i,s in enumerate(stones): #최대 힙 구현을 위해 - 로바꿔줌
            stones[i] = -s
        
        heapify(stones)
        
        while stones: # O(N)
            s1 = -heappop(stones) # 최댓값 # O(log N)
            if not stones: # stones의 마지막 값이었다면
                return s1
            
            s2 = -heappop(stones) 
            
            if s1>s2:
                heappush(stones, -(s1-s2)) # O(log N)
        
        return 0
        
Solution().lastStoneWeight([2,7,4,1,8,1])