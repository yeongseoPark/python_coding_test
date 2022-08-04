class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        answer = []
        
        if len(p) > len(s):
            return []
        
        s_slider = [0 for _ in range(26)]  # 두개의 window 비교
        p_slider = [0 for _ in range(26)]  
        # 소문자 알파벳으로만 이루어져있으니 26칸의 리스트 생성해서 개수 기록
        
        for i in p:
            p_slider[ord(i)-97] += 1
                
        start = 0
        end   = len(p)
        
        for j in range(start, end):
            s_slider[ord(s[j])-97] += 1
        
        if s_slider == p_slider:
            answer.append(start)

        while True:
            start += 1
            end   += 1
            
            if end == len(s)+1:
                break
            
            # sliding window -> 앞 한칸 없애고, 뒤 한칸 늘리고.
            s_slider[ord(s[start-1])-97] -= 1
            s_slider[ord(s[end-1])-97]   += 1
                
            if s_slider == p_slider:
                answer.append(start)
        
        return answer
Solution().findAnagrams("cbaebabacd", "abc")