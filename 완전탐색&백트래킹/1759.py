l, c = map(int, input().split())
chars = list(input().split())
chars.sort()
ans = []
moums = ['a','e','i','o','u']

def dfs(path, idx):
    if len(path) == l:
        moum = 0
        jaum = 0
        for i in path:
            if i in moums:
                moum += 1
            else:
                jaum += 1
        if moum >= 1 and jaum >= 2:
            ans.append(path)
        return
    
    for i in range(idx, len(chars)):
        dfs(path + [chars[i]], i + 1)

dfs([], 0)
for a in ans:
    print(''.join(a))
    