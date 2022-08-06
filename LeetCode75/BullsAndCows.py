from collections import Counter

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        # bulls : guess에서 맞는 위치에 있는 숫자 개수
        # cows  : guess에서 비밀 숫자 안에 있는 수는 맞지만, 잘못된 위치에 있는 경우
        # cows에 있는 값은 자리를 맞게 조정하면 bulls 에들어갈 수 있다
        
        counter = Counter(secret)
        
        bulls = 0
        cows  = 0
        
        for i in range(len(secret)):
            if guess[i] in secret and counter[guess[i]] > 0:
                if guess[i] == secret[i]:
                    bulls += 1
                    counter[guess[i]] -= 1
                    
        for i in range(len(secret)):
            if guess[i] in secret and counter[guess[i]] > 0:
                if guess[i] != secret[i]:
                    cows += 1
                    counter[guess[i]] -= 1
        
        return str(bulls)+"A"+str(cows)+"B"


    # 다른 풀이
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls = 0
        cows  = 0
        numbers = [0 for _ in range(10)]
        
        
        for i in range(len(secret)):
            s = int(secret[i])
            g = int(guess[i])
            
            if s == g:
                bulls += 1
            
            else:
                if numbers[s] < 0: # missed g가 s와 만남
                    cows += 1 
                if numbers[g] > 0: # missed s가 g와 만남 
                    cows += 1
                
                numbers[s] += 1
                numbers[g] -= 1
                
            
                    
        return str(bulls) + "A" + str(cows) + "B"   