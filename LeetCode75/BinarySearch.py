# https://leetcode.com/problems/binary-search/
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end   = len(nums)-1
        
        while start <= end:
            middle = (start+end)//2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                end = middle-1
            elif nums[middle] < target:
                start = middle+1
        
        return -1

Solution().search( [-1,0,3,5,9,12], 9)