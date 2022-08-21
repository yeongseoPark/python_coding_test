# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        length = 1
        
        tmp = head
        
        while True:
            if not head.next:
                break
            
            head = head.next
            length += 1
        
        if length == 1: # head = [1], n = 1
            return None
                
        if length-n-1<0: # 첫번째 요소를 건너뛰려는 경우
            tmp=tmp.next
            return tmp
        
        tmp2 = tmp

        for _ in range(length-n-1):
            tmp = tmp.next
        
        tmp.next = tmp.next.next
        
        return tmp2
            
            
        
    def removeNthFromEnd2(self, head, n): # head를 고정하고 더미노드를 움직이는 방법
        fast = slow = head
        for _ in range(n):
            fast = fast.next 
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next # n칸 앞서나간 fast
            slow = slow.next # fast에서 n칸 뒤떨어진 slow
        """
        slow는 fast로 부터 n만큼 뒤쳐져 있기에
        fast 시작점 한칸 전에서 멈춤(제거하려는 노드 전)
        """

        slow.next = slow.next.next
        return head