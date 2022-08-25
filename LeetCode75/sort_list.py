# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        def get_mid(head):
            mid_prev = None
            while head and head.next:
                mid_prev = head if not mid_prev else mid_prev.next
                head = head.next.next
            
            mid = mid_prev.next
            mid_prev.next = None
            return mid
        
        def merge(list1, list2):
            dummyHead = ListNode()
            tail = dummyHead
            while list1 and list2:
                if list1.val < list2.val:
                    tail.next = list1
                    list1 = list1.next
                    tail  = tail.next
                else:
                    tail.next = list2
                    list2 = list2.next
                    tail = tail.next
            
            if list1:
                tail.next = list1
            else:
                tail.next = list2
            
            return dummyHead.next
        
        mid  = get_mid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return merge(left, right)
    

        