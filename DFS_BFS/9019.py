from collections import deque

def parse(num):
    arr = deque()
    tmp = num
    
    progress = 0
    while tmp > 0:
        arr.appendleft(tmp % 10)
        tmp = tmp // 10
        progress += 1
    
    if progress < 4:
        for i in range(4-progress):
            arr.appendleft(0)
    
    return arr

def D(num):
    ans = (num * 2) % 10000
    return ans
def S(num):
    if num == 0:
        return 9999

    return num - 1
    
def L(num):
    parsed = parse(num)
    first = parsed.popleft()
    parsed.append(first)
    
    ans = 0
    for i in range(4):
        ans += parsed[i] * (10 ** (3-i))
    
    return ans
    

def R(num):
    parsed = parse(num)
    last = parsed.pop()
    parsed.appendleft(last)
    
    ans = 0
    for i in range(4):
        ans += parsed[i] * (10 ** (3-i))
    
    return ans


def bfs(start, end):
    q = deque()
    q.append(("", start))
    visited = set()
    visited.add(start)
    
    while q:
        command, tmp = q.popleft()
        
        if tmp == end:
            print(command)
            return

        d = D(tmp)
        if d not in visited:
            q.append((command + "D",  d))
            visited.add(d)
        
        s = S(tmp)
        if s not in visited:
            q.append((command + "S",  s))
            visited.add(s)
        
        l = L(tmp)
        if l not in visited:
            q.append((command + "L",  l))
            visited.add(l)
        
        r = R(tmp)
        if r not in visited:
            q.append((command + "R",  r))
            visited.add(r)


for _ in range(int(input())):
    a, b = map(int, input().split())
    
    bfs(a, b)