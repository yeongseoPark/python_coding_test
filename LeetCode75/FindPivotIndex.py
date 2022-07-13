# https://leetcode.com/problems/find-pivot-index/
class Solution(object):
    def pivotIndex(self, nums): 
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            all_sum = sum(nums)
            
            if i ==0:
                if 0 == all_sum -nums[0]:
                    return i
            elif i == len(nums) -1:
                if 0 == all_sum -nums[-1]:
                    return i
            else:
                if sum(nums[:i]) * 2 == all_sum -nums[i]:
                    return i
        
        return -1

    def pivotIndex(self, nums): # 시간 O(1) 풀이
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, sum(nums)
        
        for idx, num in enumerate(nums):
            if left == right-num:
                return idx
            
            left  += num
            right -= num
        
        return -1