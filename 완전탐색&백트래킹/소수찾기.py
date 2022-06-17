from itertools import permutations
import math
# 주어진 숫자의 제곱근 이하까지만 나누어봐도 소수인지 아닌지 판별할 수 있다!!!!!
# n = n의 제곱근보다 작은 수 * n의 제곱근보다 큰 수 & 좌항의 대칭 이기에 그렇다
# 검사량을 줄이기 위해 제곱근 이하까지만 확인


def solution(numbers): # 2,10 테스트케이스 시간초과 -> 1~i모두를 확인해서! 
    number = []
    for i in range(1,len(numbers)+1): # 1~numbers자릿수
        for i in (permutations(numbers,i)): # 순열 구해서
            number.append(''.join(i)) # number리스트에 str로 추가
    print(number)

    real_answer= 0
    for i in set(map(int,number)): # number리스트 요소 int로 바꾸어서
        # 이때 set을 써서, 불필요한 숫자의 중복을 제겋마
        cnt = 0
        if i != 0 and i != 1: # i가 0이거나 1이면 소수가 될 수 없음 
            for j in range(2,int(math.sqrt(i))+1):
                if i % j == 0:
                    cnt += 1 # 2~i의 제곱근(정수) 에서 나눠지는 값 확인
            # 이게 0이면(1이랑 자기 자신 말고 안나눠지면) 소수인것
            if cnt == 0:
                real_answer += 1

    return real_answer


# def solution(numbers): # 2,10 테스트케이스 시간초과 -> 1~i모두를 확인해서! 
#     number = []
#     for i in range(1,len(numbers)+1): # 1~numbers자릿수
#         for i in (permutations(numbers,i)): # 순열 구해서
#             number.append(''.join(i)) # number리스트에 str로 추가
#     print(number)

#     real_answer= 0
#     for i in set(map(int,number)): # number리스트 요소 int로 바꾸어서
#         # 이때 set을 써서, 불필요한 숫자의 중복을 제겋마
#         cnt = 0
#         for j in range(1,i+1):
#             if i % j == 0:
#                 cnt += 1 # 1~i에서 나눠지는 값 확인
#         # 이게 2(자기자신이랑 1) 이면 소수인겨
#         if cnt == 2:
#             real_answer += 1

#     return real_answer
    
solution("011")