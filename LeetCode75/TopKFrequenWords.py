from collections import Counter

class Solution(object):
    def topKFrequent(self, words, k): # O (N log N)
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        count  = Counter(words)
        
        result = sorted(count, key = lambda word: (-count[word], word)) # 1차 정렬기준 빈도 내림차순(값), 2차 사전순(키)
        
        return result[:k]

