class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        dic = {
            "0" : 0,
            "1" : 1,
            "2" : 2,
            "3" : 3,
            "4" : 4,
            "5" : 5,
            "6" : 6,
            "7" : 7,
            "8" : 8,
            "9" : 9
        }
        
        def convert(num):
            leng = len(num)
            
            res = 0
            
            for i in range(leng):
                res += 10 ** (leng-1-i) * dic[num[i]]
            
            return res
        
        num_one = convert(num1)
        num_two = convert(num2)
        
        return (str) (num_one * num_two)