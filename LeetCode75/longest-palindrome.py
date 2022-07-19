# https://leetcode.com/problems/longest-palindrome/submissions/

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 좌우대칭 문자는 좌 (중간) 우  형태인데
        # 좌 와 우 의 문자의 갯수가 같다는 점을 이용
        
        if len(s) == 1: # 길이 1이면 palindrome
            return 1
        
        dic = {}
        for i in set(list(s)): 
            dic[i] = list(s).count(i) # 딕셔너리에 s의 값:출현빈도
            
        ans = 0
        for i in dic:
            if dic[i] > 1: # 두개 이상 있어서 좌,우에 분배할 수 있다면
                ans += (dic[i] // 2) * 2 # 쌍의 갯수 구하고, 거기에 2곱함
                dic[i] -= (dic[i] // 2) * 2 # 그만큼 딕셔너리에서 빼줌
        
        if max(dic.values()) > 0:
            return ans + 1
        else:
            return ans

        # 다른방법 : set()을 통해 s의 문자들 중 홀수번 나오는 것을 센다
        ss = set()
        for letter in s: # letter가 홀수번 나오면 ss 에 있고, 짝수번이면 ss에 없다
            if letter not in ss:
                ss.add(letter) 
            else:
                ss.remove(letter)

        if len(ss) != 0: # s길이 - 홀수번 나오는 letter개수   
            return len(s) - len(ss) + 1 # +1 해주는 이유는, 가운데에 하나 넣을 수 있기때문
        else: # 싹 다 짝수번 나오는 경우
            return len(s)
                
        