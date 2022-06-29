# # https://leetcode.com/problems/palindrome-number/

class Solution(object):  
    # Follow up : int를 string으로 바꾸지 않고 풀기
    def isPalindrome(self, x):
        compare = x
        if x < 0: # 음수면 - 때문에 뒤집어서 같을수가 없다
            return False

        digit = 0 # 자릿수
        for i in range(10):
            if x >= 10**i and x < 10**(i+1): 
                # 1024면 10^3보다 크고 10^4보다 작으니까
                # digit 은 3(세자리수가 아니라 10의 3승 자릿수)
                digit = i
        
        lst = [] # 각 자릿수에 해당하는 값 넣는다(큰 자릿수부터)
        for i in range(digit, -1 , -1):
            num = x//10**i 
            lst.append(num) 
            x -= num * 10**i
        

        result = 0
        for i in range(digit, -1, -1): # n * 10^m 에서 n을 뒤집어 줘서 숫자 뒤집ㅇㅁ
            result += lst[i]*(10**i)
        
        if result == compare:
            return True
        else:
            return False

# discussion 답변
class Solution(object):  
    def isPalindrome(self, x):
        if x < 0 or (x>0 and x % 10== 0): # 음수거나, 자연수이면서 끝자리0이면(앞자리도 0이어야 palindrome인데 그러기 불가능)
            return False 
        
        result = 0  
        while x > result: # 전체가 아니라 반만 잘라서 같은지 확인(overflow방지)
            result = result * 10 + x % 10 # x의 뒷자리부터 하나씩 가져오는 result
            # 1331 0
            # 133 1
            # 13 13
            x //= 10
        
        if x == result or x == result//10: # 앞조건은 짝수일때, 뒷 조건은 홀수 일때
            return True
        else:
            return False

print(Solution().isPalindrome(0))
