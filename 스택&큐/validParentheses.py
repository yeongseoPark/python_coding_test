class Solution(object):
    def isValid(self, s):
        if len(s) % 2 != 0:
            return False

        dic = {
            "(" : ")" ,
            "{" : "}" ,
            "[" : "]" 
        }
        
        stack = []
        
        for i in s:
            if i == "{" or i == "(" or i == "[": # 괄호 앞자리 나왔을때
                stack.append(dic[i]) # 뒷자리 스택에 넣어줌
            else: # 괄호 뒷자리 나왔을때
                if stack: # 스택이 있다면
                    if stack[-1] == i: # 만약 가장 최근 앞자리와 현재 i 가 같으면 
                        stack.pop() # 스택 맨위빼줌
                    else: # 다르면 잘못된것
                        return False
                else: # 스택이 없다면(뒷자리부터 나온 경우)
                    return False
            
        if len(stack) == 0: 
            return True
        else:
            return False

    
    # 스택 사용한 더 짧은 코드          
    def isValid(self,s):
        stack = []
        dict  = {"]":"[", ")":"(", "}":"{"}

        for char in s:
            if char in dict.values(): # 괄호 앞자리일경우
                stack.append(char) # 스택에 넣어줌
            
            else: # 괄호 뒷자리일경우
                if stack == [] or stack.pop() != dict[char]:
                    return False
            
        return stack == []


print(Solution().isValid("([")) 