class Solution(object): 
    def strStr(self, haystack, needle): # 1
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        
        return haystack.find(needle)

    def strStr(self, haystack, needle): # 2
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        
        leng = len(needle)
        
        for i in range(len(haystack)-leng+1):
            if haystack[i:i+leng] == needle: # haystack의 복제본을 만들고 이를 비교하기 때문에 여기서 O(leng)의 복잡도 소요
                return i
        
        # 따라서 O(len(needle)*len(haystack))의 시간복잡도 걸림
        return -1
        