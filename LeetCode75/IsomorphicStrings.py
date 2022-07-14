# https://leetcode.com/problems/isomorphic-strings/

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        def toNum(s):
            num = 1
            dic = {}
            new = [0] * len(s)
            for i in range(len(s)): # 여기서 O(n)
                if s[i] in dic:
                    new[i] = dic[s[i]]
                else:
                    dic[s[i]] = num
                    new[i] = num
                    num += 1
            
            return new
        
        s1 = toNum(s)
        t1 = toNum(t)
        
        if s1 == t1: # 비교하는데 O(n)
            return True
        return False 
                    
    def isIsomorphic(self, s, t): # O(n)으로 훨씬 빠른 풀이
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(set(t)) != len(set(s)): # 구성 요소 숫자 다른경우 
            return False
        
        dic = {}
        for i in range(len(t)):
            if t[i] not in dic:
                dic[t[i]]  = s[i] # t[i]와 s[i]를 매핑 
            elif dic[t[i]] != s[i]:
                return False
        
        return True 