# https://leetcode.com/problems/is-subsequence/

class Solution(object): # 답 봄 ㅠㅠ
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """ 
        i , j = 0 , 0 # s, t 각각의 인덱스 : 투포인터
        
        while i < len(s) and j < len(t): # s, t 중 하나를 다 확인하면 끝
            if s[i] == t[j]: # s의 인덱스 올려가며 t안에 있는지 확인 
                print(i)
                i += 1 
            
            j += 1
        
        return i == len(s)
        
        

print(Solution().isSubsequence("ab","abbbbbbc")) # 이경우 i=2에서 while문 탈출