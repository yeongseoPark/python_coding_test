# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        
        odd  = head
        even = head.next
        evenhead = even # odd와 even 이어붙이기 위함
        # 포인터 세개만 필요하고 추가공간 X : O(1) space
        
        while even and even.next:
            odd.next  = even.next
            odd       = odd.next
            
            even.next = odd.next
            even      = even.next
        
        odd.next = evenhead
        
        return head
            
            