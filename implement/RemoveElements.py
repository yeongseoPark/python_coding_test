# https://leetcode.com/problems/remove-element/submissions/
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for i in range(nums.count(val)):
            nums.remove(val)
        
        return len(nums) - nums.count(val)