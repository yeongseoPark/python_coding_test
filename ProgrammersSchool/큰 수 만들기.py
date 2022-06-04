def solution(number, k):
    number = list(number)
    stack = list()
    for num in number:
        while stack and stack[-1] < num and k > 0:
            # num보다 stack의 마지막 요소가 작고(그래서 교체돼야하고), 아직 교체횟수가 남아있고, 스택에 요소가 있는동안엔
            stack.pop()
            k -= 1
        stack.append(num)

    if len(stack) != len(number)-k:
        for i in range(len(stack)-len(number)+k):
            stack.pop()
    # 반례: 5432의 경우, pop일어나지 않고 모두 append됨.
    # 이런경우는 제거하려고 했던만큼 강제로 pop해줘야 함 
    
    return ''.join(stack)



print(solution("1924",2))