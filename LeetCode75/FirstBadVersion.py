# https://leetcode.com/problems/first-bad-version/submissions/
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end   = n
        
        while start <= end:
            middle = (start + end) // 2
            
            if isBadVersion(middle) and not isBadVersion(middle-1):
                return middle
            elif not isBadVersion(middle):
                start = middle + 1
            elif isBadVersion(middle) and isBadVersion(middle-1):
                end = middle -1