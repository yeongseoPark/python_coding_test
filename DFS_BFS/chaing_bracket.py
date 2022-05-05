# https://programmers.co.kr/learn/courses/30/lessons/60058

def balanced_index(p): # 균형잡힌 괄호 문자열 의 인덱스 반환
    count = 0 # 왼쪽 괄호 ( 의 개수
    for i in range(len(p)):
        if p[i] == "(": #( 이면 count += 1
            count += 1
        else:           #) 이면 count -= 1
            count -= 1
        if count == 0:  # ( 와 ) 개수 맞으면 - 더하고,빼서 0 되면
            return i    # 해당 인덱스 반환
    
def check_proper(p): # 균형잡힌 문자열일때, 올바른 괄호 문자열인지 판단 -> ( 와 )의 개수가 맞고, 짝도 맞으면
    count = 0 # 왼쪽 괄호의 갯수
    for i in p: 
        if i == '(': # i가 ( 이면
            count += 1
        else:        # i가 ) 일때
            if count == 0:  # 만약 count가 0, 즉 직전이 (가 아니면 False => ")" 가 먼저 나온 경우 이 조건에 걸림
                return False
            count -= 1
    # )차례에서 count=0아니면, 19번째 줄에 걸리지 않으면 True반환
    return True

def solution(p):
    answer =''
    if p == '':
        return answer # 빈 문자열인 경우 그대로 반환
    index = balanced_index(p) #균형잡힌 괄호 문자열의 인덱스 반환
    u = p[:index + 1]  # 균형잡힌 괄호 문자열 u
    v = p[index+1:]    # u뒤의 나머지 문자열(빈문자열도 될 수 있음)

    if check_proper(u): # u가 올바른 괄호문자열 이라면
        answer = u + solution(v) # 재귀적으로 v에 대해 solution을 다시 실행
    
    else:   # u가 올바른 괄호문자열이 아니라면
        answer= '('  # 반환할 빈 문자열에 (를 붙임
        answer += solution(v) #문자열 v에 대해 재귀적으로 solution실행한 결과 붙임
        answer += ')' # )를 다시 붙임
        u = list(u[1:-1]) # u에서 첫번째(0)과 마지막 문자 제거,
        for i in range(len(u)): 
            if u[i] == '(': # 첫번째와 마지막 제외한 u에서 괄호 방향을 뒤집음 
                u[i] = ')'  
            else:
                u[i] = '('
        answer += "".join(u) # 이를 뒤에 붙임
    return answer

EX : "()))(("
1. u="()" , v= "))((" # v에 대해 재귀적으로 solution진행. 이때 answer = "()"
2. u="))((" v="" #u가 올바른 문자열 아니기에 36이하 라인 진행
3. answer = "(", solution(v)는 빈값 리턴
4. answer = "()"
5. u의 첫,마지막 문자 제거하고 나머지 문자열 뒤집어서 붙임 
6. answer = "()" +  "()"
결과적으로 ()()()

# print(solution("()))(("))