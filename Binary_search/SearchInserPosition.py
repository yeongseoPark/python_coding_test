class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end   = len(nums)-1
        while end >= start:
            mid = (start+end) //2
            
            if nums[mid] > target:
                end   = mid-1
            elif nums[mid] < target:
                start = mid +1
            else:
                return mid
        
        if target > nums[mid]:
            return mid+1
        else:
            return mid


