n = int(input())

cnt = 0
moves = []
def hanoi(n, a, c):
    global cnt
    if n == 1: # n이 1이면 그냥 옮기면 됨
        cnt += 1
        moves.append(str(a) + " " + str(c))
        return
    
    hanoi(n-1, a, 6-a-c) # n-1개 중간기둥으로 
    hanoi(1, a,c) # 맨 밑에거 목적지 기둥으로 
    hanoi(n-1, 6-a-c, c) # 중간기둥의 n-1개 목적지 기둥으로

hanoi(n, 1,3)
print(cnt)
for i in moves:
    print(i)