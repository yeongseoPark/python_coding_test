N= int(input())

if N < 10:
    print(N)
    exit()

decreases = []
def dfs(dec, num ,depth): # 만들어지고 있는 감소숫자의 배열(문자열구성) , 감소 시작하는 숫자, 깊이
    
    decreases.append(int("".join(dec))) # 현재 감소숫자를 decreases 배열에 넣음
    
    if depth == 10: # 10 깊이 들어갔으니 더이상 탐색 X
        return
    
    for i in range(int(num) - 1, -1, -1): 
        dfs(dec + [str(i)], str(int(i)) , depth + 1)

# 9로 시작하는 감소 숫자 ~ 0으로 시작하는 감소숫자 모두 decreases 배열에 넣음
for i in range(9, -1, -1):
    dfs([str(i)], str(i), 1) # join 편하게 str로 넣음

# 해당 배열 정렬
decreases.sort()

# 배열 길이보다 N(번째수)가 높으면 없는 것
if N > len(decreases) - 1:
    print(-1)
else:
    print(decreases[N])