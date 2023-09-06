class Solution(object):
    def lemonadeChange(self, bills):
        left = dict()
        left[5]  = 0
        left[10] = 0
        left[20] = 0

        for p in bills:
            if p == 5:
                left[5] += 1

            elif p == 10:
                if left[5] <= 0:
                    return False
                else:
                    left[5] -= 1
                    left[10] += 1

            elif p == 20:
                if left[5] <= 0 or left[10] <= 0:
                    if left[5] >= 3:
                        left[5] -= 3
                        left[20] += 1
                    else:
                        return False

                else:
                    left[5] -= 1
                    left[10] -= 1 
                    left[20] += 1
        
        return True