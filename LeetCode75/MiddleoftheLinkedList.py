# https://leetcode.com/problems/middle-of-the-linked-list/submissions/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tmp = head
        
        cnt = 0
        while head:
            head = head.next
            cnt += 1
        
        for i in range(cnt//2):
            tmp = tmp.next
        return tmp
            

