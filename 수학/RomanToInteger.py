class Solution(object):
    def romanToInt(self, s):
        symbols = {"M": 1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
        outlier = {"IV":4, "IX": 9, "XL":40, "XC":90, "CD":400, "CM":900}
        
        toint = 0
        
        for i in range(len(s)):
            next_two = s[i] + s[i+1] if i < len(s) -1 else None
            if next_two not in outlier:
                toint += symbols[s[i]]
            else:
                toint += outlier[s[i]+s[i+1]]
                toint -= symbols[s[i+1]] 
                # 4와 9를 처리하기 위해 두칸을 썼으니, 이를 고려해서 i다음칸은 없는 일로처리해야함
            
            
        
        return toint

print(Solution().romanToInt("MCMXCIV"))