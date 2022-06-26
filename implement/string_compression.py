# https://programmers.co.kr/learn/courses/30/lessons/60057
# 문자열에서 같은 값 연속해서 나타나는 것을 그 문자 개수와 반복된느 값으로 압축
#  "aabbaccc"의 경우 "2a2ba3c"
# 반복되는 문자 적은 경우 압축률이 낮다
# 이를 해결하기 위해 문자열을 1개 이상의 단위로 잘라서 압축
# 예를 들어, "ababcdcdababcdcd"의 경우 문자를 1개 단위로 자르면 전혀 압축되지 않지만, 2개 단위로 잘라서 압축한다면 "2ab2cd2ab2cd"로 표현할 수 있습니다
# 8개 단위로 잘라서 압축한다면 "2ababcdcd"로 표현, 이때가 가장 짧게 압축한 것

# s = input() # 1<=s<=1000 / 알파벳 소문자로만 이루어짐
# # 1개 이상 단위로 문자열을 잘라 압축하여 표현한 것 중 가장 짧은 것의 길이 return
# # 문자열은 제일 앞부터 정해진 길이만큼 잘라야 합니다.

# # 자를 수 있는 최대 길이수 = len(s) // 2
# # 자를 수 있는 길이 수 다 잘라보고 젤 짧은것 선택

# # 1
# def solution(s):
#     answer = len(s)

#     for step in range(1, len(s)//2+1):
#         compressed = ""
#         prev = s[0:step] # 앞에서부터 step 만큼의 문자열 추출
#         count = 1
#         # 1 단위(step)부터 압축 단위 늘려가며 확인
#         for j in range(step, len(s), step): #압축하는 단어 수 만큼 증가하게(2면은 2 4 6...)
#             # prev(이전)과 그 다음이 같으면 압축 횟수 증가
#             if prev == s[j:j+step]:
#                 count += 1
#             # prev와 그 다음이 달라서 압축이 안되면
#             else:
#                 compressed += str(count) + prev if count >= 2 else prev
#                 prev  = s[j:j+step] # prev상태 초기화
#                 count = 1
#         # 남아있는 문자열 처리(len(s) % step)
#         compressed += str(count) + prev if count >= 2 else prev

#         answer = min(answer,len(compressed)) # 더 작은것 선택(for문 돌리며 자를 수 있는 경우 중 가장 작은것이 answer되게됨)

#     return answer


def solution(s):
    answer = []
    for i in range(1,len(s)//2+1):
        comp  = ""
        front = 0
        back  = i
        
        count = 1
        while True:
            if back > len(s) - 1:
                if count > 1:
                    comp += str(count) + s[front-i:back-i]
                else:
                    comp += s[front:]
                break
                
            if s[front:back] == s[back:back+i]:
                count += 1
                front += i
                back  += i
            else:
                if count == 1:
                    comp += s[front:back]
                else:
                    comp  += str(count) + s[front:back]
                count =  1
                front += i
                back  += i
                
        answer.append(comp)

    print(answer)
    answer.sort(key=len)
    
    return len(answer[0])

print(solution("ababcdcdababcdcd"))