# # https://leetcode.com/problems/two-sum/submissions/

class Solution(object): 
    def twoSum(self, nums, target):
#         # O(n^2)보다 나은 방식으로 풀기
        dic = {}
        for i,v in enumerate(nums): # O(n)
            j = target - v # 더해서 target 되는 j
            if j in dic: # O(1)
                return [dic[j],i]
            else:
                dic[v] = i # 값:그에 해당하는 인덱스 저장

        

# 포기 ㅎㅎ 답봄
#         answer = []
#         maxy = max(nums)
        
#         if maxy >= 0:
#             for i in range(0,maxy+1):
#                 j = target - i
#                 if j == i:
#                     if nums.count(j) >1 : ## 3,3 = 6 의 경우
#                         answer.append(nums.index(i)) # 첫번째 3 인덱스
#                         answer.append(nums.index(i,nums.index(i)+1)) # 그다음 3인덱스
#                         break
                        
#                     else: #3,2,4 = 6 의 경우
#                         pass
                    
#                 else:
#                     if j in nums and i in nums:
                      
#                         answer.append(nums.index(i))
#                         answer.append(nums.index(j))
#                         break
        
#         else:
#             for i in range(min(nums)-1,0,-1):
#                 j = target - i
#                 if j == i:
#                     if nums.count(j) >1 : ## 3,3 = 6 의 경우
#                         answer.append(nums.index(i)) # 첫번째 3 인덱스
#                         answer.append(nums.index(i,nums.index(i)+1)) # 그다음 3인덱스
#                         break
                        
#                     else: #3,2,4 = 6 의 경우
#                         pass
                    
#                 else:
#                     if j in nums and i in nums:
                      
#                         answer.append(nums.index(i))
#                         answer.append(nums.index(j))
#                         break
        
        
        
#         return answer
            
# print(Solution().twoSum([-1,-2,-3,-4,-5],-8))

