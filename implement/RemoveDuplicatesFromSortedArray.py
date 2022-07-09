# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution(object):
    def removeDuplicates(self, nums): 
        """
        :type nums: List[int]
        :rtype: int
        """
        dupped = []
        
        k = len(nums)
        
        for i in nums:
            if i in dupped:
                pass
            else:
                dupped.append(i)
                nums.append(i) 
                # O(1)의 추가 공간 안에서 
                # 다른 메모리 공간을 사용하지 않고 nums를 사용해서 풀어야 해서
                # nums배열을 늘려주고 앞을 자름
        
        for i in range(k):
            nums.pop(0) # 앞에서부터 잘라서 시간 많이 소요..

        return len(nums)
    
# discuss O(n)답안
def removeDuplicates(A):
    if not A:
        return 0

    newTail = 0 # newTail을 통해 nums앞자리를 바꿔나감

    for i in range(1, len(A)):
        if A[i] != A[newTail]:  # 만약 여태까지의 값과 다르다면?
            newTail += 1        # newTail(인덱스) 하나씩 더해줌 
            A[newTail] = A[i]   # 다른 값(중복되지 않는 값) 으로 해당 인덱스 교체 

    return newTail + 1 # 길이 리턴해야하므로 인덱스인 newTail + 1

removeDuplicates([0,0,1,1,1,2,2,3,3,4])



