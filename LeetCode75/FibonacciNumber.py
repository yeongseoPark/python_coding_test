class Solution(object): # 1. Bottom-up 방식
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """        
        memo = [0,1]
        
        if n == 0 or n == 1: # 이게 없으면 while문 빠져나오질 못함
            return memo[n]
        
        fib = 2
        
        while True:
           
            memo.append(memo[fib-1] + memo[fib-2])
            
            if fib == n:
                break
            
            fib += 1
        
        return memo[n]
    

class Solution(object): # Top-down(재귀) 방식
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """        
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        return self.fib(n-1)+ self.fib(n-2)