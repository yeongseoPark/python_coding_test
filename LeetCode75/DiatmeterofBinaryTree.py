# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        answer = []
        
        def getDepth(node):
            if not node:
                return 0
            return 1 + max(getDepth(node.left), getDepth(node.right))
        
    
        def inorderTraversal(root, answer):

            if root is None:
                return

            inorderTraversal(root.left, answer)
            answer.append(getDepth(root.left) + getDepth(root.right))
            inorderTraversal(root.right, answer)
        
        inorderTraversal(root, answer)
        
        return max(answer)
        
        
        # 모든 노드에 대해 밑의 연산을 해줘서 그것의 최댓값을 리턴해야 함
        # return getDepth(root.left) + getDepth(root.right)