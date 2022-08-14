class Solution(object):
    def isHappy(self, n): # 사이클 찾기, 재귀 버젼
        """
        :type n: int
        :rtype: bool
        """
        dic = {}
        
        def sum(n):
            tmp = []
            new = 0
            while True:
                if n == 0:
                  break
                else:
                    tmp.append(n % 10)
                    n //= 10

            for i in tmp:
                new += i ** 2
            
            if new in dic:
                return False
            else:
                if new == 1:
                    return True
                dic[new] = 1
                return sum(new)
        
        return sum(n)
    
    def isHappy(self, n): # 반복문 버젼
        """
        :type n: int
        :rtype: bool
        """
        mem = set()
        
        while n != 1:
            n = sum([int(i) ** 2 for i in str(n)])
            if n in mem:
                return False
            else:
                mem.add(n)
        
        return True
        
        
            