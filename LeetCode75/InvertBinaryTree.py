# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        
        def invert(root):
            if not root.left and not root.right:
                return 

            elif root.left and root.right:
                tmp = root.right
                root.right = root.left
                root.left  = tmp

                return invert(root.right) ,invert(root.left)

            elif root.left and not root.right:
                root.right = root.left
                root.left = None
                return invert(root.right)

            elif root.right and not root.left:
                root.left = root.right
                root.right = None
                return invert(root.left)
        
        invert(root)
        
        return root