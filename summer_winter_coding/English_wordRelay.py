# https://programmers.co.kr/learn/courses/30/lessons/12981

# 가장 먼저 탈락하는 사람의 번호와, 그 사람이 자신의 몇번째에 탈락하는지 구해서 return [번호,차례]
# 탈락은 1. 끝말이 안이어지거나 2.이전에 등장했던 단어 또 사용하는 경우

# 1.
def solution(n, words):
    answer = [0,0]
    idx    = -1

    while idx +1 <len(words):
        idx += 1
        if idx > 0 and words[idx-1][-1] != words[idx][0] or words[idx] in words[:idx]: #끝말이 맞지 않거나, 이전에 현재 단어와 같은 단어가 있는 경우
            # 밑에서는 각 조건을 다른 높이에서 for문 돌려서 테스트케이스에 계속 걸렸다면, 여기서는 그런 일 없게 or로 묶어줌
            answer = [(idx % n)+1 , idx // n + 1] # 사람 번호, 그의 차례
            break
    return answer 





# 2.
# def solution(n, words):
#     for i in words:
#         if words.count(i) > 1: #특정 단어가 반복될 시
#             first = words.index(i)
#             second = words.index(i, first+1) + 1 
            
#             talker = n if second % n == 0 else second % n # 발언자
#             nth    = (second // n) + 1 if talker != n else second // n 
#             return [talker,nth]

#     for i in range(len(words)-1): # 1 
#         if words[i][len(words[i])-1] != words[i+1][0]:
#             talker = n if (i+2) % n == 0 else (i+2) % n # ex) n=3, 9번째면 3번째가 발언자, 8째면 8%3 == 2번째 
#             # 발언자: 발언의 순서가 발언자의 수로 딱 나눠떨어지면 마지막 발언자, 아니면 그 나머지
#             nth    = ((i+2) // n) +1 if talker != n else (i+2)//n # 몇번째 
#             # ex) n=3 , talker가 2일때 i+1(문제가 되는 인덱스)+1이 8이면 이를 3으로 나누면 몫이 2임, 실제로는 세번째이므로 여기다 1을 더해주면 됨
#             return [talker,nth]
    
#     return [0,0]
# print(solution(4,['aa', 'aba', 'aba', 'aa','ror']))
# # 테스트 19번 통과못함..