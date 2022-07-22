# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        
        if root.val < p.val and root.val < q.val: 
            # 바로위의 조상이 아니라면 root의 값은 p,q 보다 아예 작거나 -> right 재귀적으로 탐색
            return self.lowestCommonAncestor(root.right, p, q)
        
        elif root.val > p.val and root.val > q.val:
            # p,q보다 아예 크다 -> left 재귀적으로 탐색
            return self.lowestCommonAncestor(root.left, p, q)
        
        elif min(p.val, q.val) <= root.val and root.val <= max(p.val, q.val):
            # LCA라면 p와 q 사이에 root가 위치한다
            return root