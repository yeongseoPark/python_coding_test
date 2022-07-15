# https://leetcode.com/problems/merge-two-sorted-lists/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        cur = dummy= ListNode() # dummy로 merge된 연결리스트의 처음을 가리킨다
        
        while list1 and list2: # list1과 list2는 연결리스트를 가리키는 "포인터"
            
            if list1.val < list2.val: # 오름차순이니까 더 작은 것 선택
                cur.next   = list1  
                cur        = cur.next # cur도 바꿔준다 -> cur을 바꿔주지 않으면 linkedList가 앞으로 나아가지 않음
                list1      = list1.next # list1의 맨 앞 요소를 선택했으니, list1을 가리키는 포인터도 한칸 나아간다
            else:
                cur.next   = list2 
                cur        = cur.next
                list2      = list2.next
        
        if list1 or list2:
            cur.next = list1 if list1 else list2
            cur      = cur.next
        
        
        return dummy.next # dummy는 while문을 돌며 cur에 추가되는 first node를 가리키고 있다
