"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object): # dfs
    # iterative로 품
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root == None:
            return []
        
        visited = []
        stack   = [root]
        
        while(stack):
            
            node = stack.pop()
            visited.append(node.val)
            stack.extend(node.children[::-1])
        
        return visited
    
    # 재귀로 푼 버전 
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        visited = []
        
        self.dfs(root, visited)
        
        return visited
    
    def dfs(self, root, visited):
        if root is None:
            return 
        
        visited.append(root.val)
        
        for children in root.children: # 3 2 4 의 형태
            self.dfs(children, visited)