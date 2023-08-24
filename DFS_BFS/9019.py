from collections import deque



def D(num):
    ans = (num * 2) % 10000
    return ans

def S(num):
    if num == 0:
        return 9999

    return num - 1
    
def L(num):
    return (num % 1000) * 10  + num // 1000
    

def R(num):
    return (num % 10) * 1000 + num // 10
    


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