# https://leetcode.com/problems/binary-tree-level-order-traversal/

from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        deq = deque()
        deq.append(root)
        visited= [] 
        
        
        while deq:
            cur_level = [] # 한 층의 값을 담을 리스트
                            
            for i in range(len(deq)): # deq에는 한 층의 노드들만 다 들어있는 상황
                # 한 층 노드들의 갯수만큼 반복하며, 밑의층 자식들 deq에 넣고, visited에 추가할 [층의 값 리스트] 만듬
                node = deq.popleft()
                if node.left : 
                    deq.append(node.left)
                if node.right:
                    deq.append(node.right)
                cur_level.append(node.val)
            visited.append(cur_level)
            
        return visited