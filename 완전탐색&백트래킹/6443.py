def dfs(cur, cnt):
    if cnt == len(word):
        used.append(cur)
        return 

    for i in range(26):
        if visited[i] >= 1:
            visited[i] -= 1
            dfs(cur + chr(i+97), cnt+1)
            visited[i] += 1

for i in range(int(input())):
    word = list(input().rstrip())
    word.sort()
    
    used = list()
    visited = [0] * 26
    for i in word:
        visited[ord(i) - 97] += 1        
    
    dfs("", 0)
    
    for i in list(used):
        print(i)
    