# https://leetcode.com/problems/decode-string/

class Solution(object): # 답봄
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        curNum = 0
        curString = ""
        
        for i in s:
            if i == "[":
                stack.append(curString)
                stack.append(curNum)
                curString = ""
                curNum = 0
            
            elif i == "]":
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num*curString
            
            elif i.isdigit(): # 숫자
                curNum = curNum*10 + int(i) # 101[Leetcode]처럼 숫자가 한자리수 이상인 경우
            
            else:             # 문자
                curString += i
        
        return curString