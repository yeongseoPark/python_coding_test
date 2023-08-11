import sys
from collections import deque
input = sys.stdin.readline

for i in range(int(input())):
    p = input().rstrip()
    n = int(input()) # 배열의 길이
    arr = input().rstrip()[1:-1].split(',')
    q = deque(arr)  # [] 라고 입력받아도 deque의 길이는 1됨

    rev, front, back = 0, 0 , len(q) - 1
    flag = 0
    if n == 0:
        q = []
        back = 0
    
    for j in p:
        if j == "D":
            if len(q) < 1:
                print("error")
                flag = 1
                break
            
            if rev % 2 == 0:
                q.popleft()
            else:
                q.pop()

        else: # R
            rev += 1
    
    if not flag:
        if rev % 2 == 0:
            print("[" + ",".join(q) + "]")
        
        else:
            q.reverse()
            print("[" + ",".join(q) + "]")
            