class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        stack = []
        for i in s:
            if i == "#":
                if len(stack) != 0:
                    stack.pop()
                else:
                    pass
            else:
                stack.append(i)
        
        stack2 = []
        for i in t:
            if i == "#":
                if len(stack2) != 0:
                    stack2.pop()
                else:
                    pass
            else:
                stack2.append(i)

        print(stack)
        print(stack2)
        
        if stack == stack2:
            return True
        else:
            return False

print(Solution().backspaceCompare("a##c","#a#c"))