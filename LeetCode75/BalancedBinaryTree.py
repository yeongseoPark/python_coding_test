# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        def getDepth(node):
            if not node:
                return 0
            return 1 + max(getDepth(node.left), getDepth(node.right))
        
        
        return abs(getDepth(root.left) - getDepth(root.right)) <= 1 \
            and self.isBalanced(root.left) and self.isBalanced(root.right)
        # 1. root가 height-balanced인지 체크한다 
            # getDepth는 자신을 포함한 트리의 층수를 리턴
            
        # 2. left가 height-balanced인지 재귀[self.isBalanced(root.left)] 를 통해 체크한다
        # 3. right도 마찬가지
        
            