from collections import Counter

class Solution(object):
    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        counter = Counter(words)
        
        seen = set()
        
        result = 0
        center = False
                
        for word in counter:
            if word in seen: # 한번 확인한 단어는 더이상 확인 x
                continue
            
            reversed = word[::-1]

            if reversed in counter: 
                if reversed != word: # cl, lc 같은 경우 
                    result += 4*min(counter[word], counter[reversed])
                    
                else: # aa와 같은 경우 
                    result += 4*(counter[word]//2)
                    
                    # cl aa lc 처럼 가운데를 채우는 경우
                    if not center and counter[word] % 2 == 1:
                        result += 2
                        center = True
            
            seen.add(word)
            seen.add(reversed)
        
        return result