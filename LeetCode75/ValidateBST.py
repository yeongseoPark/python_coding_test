# https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root, lefty =float('-inf'), righty=float('inf')): # - 무한 / + 무한을 BST의 양쪽 경게로 삼음 
        """
        :type root: TreeNode
        :rtype: bool
        """
        # left.val < node.val < right.val
        
        if root is None: # base condition1
            return True
        
        if root.val <= lefty or root.val >= righty:   # base condition2
            return False
        
        return self.isValidBST(root.left, lefty, root.val) and self.isValidBST(root.right, root.val, righty )
