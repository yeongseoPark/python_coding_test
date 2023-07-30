import sys 
k = int(input())
inequals = list(input().split())
nums = [i for i in range(10)]

min_val = ""
max_val = ""
visited = [0] * 10

def check(i, j , inequal):
    if inequal == "<":
        return i < j
    else:
        return i > j

def dfs(path, idx):
    global min_val, max_val

    # 뒤로 갈수록 앞자리 숫자가 커져서, min_val은 맨처음한번만, max_val은 계속업데이트해주면 됨
    if idx == k+1:
        if len(min_val) == 0:
            min_val = path
        else:
            max_val = path
        return
    
    for i in range(10):
        if not visited[i]:
            if idx == 0 or check(path[-1], str(i), inequals[idx - 1]):
                visited[i] = True
                dfs(path+str(i), idx+1)
                visited[i] = False

dfs("", 0)
print(max_val)
print(min_val)
