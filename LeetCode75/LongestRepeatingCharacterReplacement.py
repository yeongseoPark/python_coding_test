# https://leetcode.com/problems/longest-repeating-character-replacement/submissions/
# 답봄

from collections import Counter

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count  = {}
        result = 0  # substring 길이
        
        left= 0
        
        # count에는 substring의 각 문자와 그것의 빈도수 저장된다
        # right - left + 1 - max(count) <= k 인 동안,
        # 즉, 현 substring 안에서, k번 교체하여 repeating charcter를 만들 수 있는 동안, 은 substring의 왼쪽은 고정되고 오른쪽이 확장한다
        
        for right in range(len(s)): # O(n)
            count[s[right]] = 1 + count.get(s[right], 0) 
            # count에 s[right]가 키로 없으면 default로 0 값 넣고, 있으면 있는 값 가져온다
            
            while (right-left+1) - max(count.values()) > k: # max() 에 O(26)이 수행된다
                # substring이 valid 하지 않는 구간
                count[s[left]] -= 1
                left += 1
                # count에서 왼쪽포인터의 값을 지우고, 왼쪽 포인터를 한칸 밀어낸다
            
            result = max(result, right-left+1)
        
        return result