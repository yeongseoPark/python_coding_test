n = int(input())

box = [[int(i) for i in str(input())] for _ in range(n)]

def quad(n, r, c): # 변의 길이, 시작행, 시작열
    check = box[r][c]
    for i in range(r, r+n):
        for j in range(c, c+n):
            if check != box[i][j]:
                check = -1
                break
    
    if check == -1:
        print("(", end="")
        quad(n // 2, r, c)
        quad(n // 2, r, c + n // 2)
        quad(n // 2, r + n // 2, c)
        quad(n // 2, r + n // 2, c + n // 2)
        print(")", end="")
    
    elif check == 1:
        print(1, end = "")
        
    elif check == 0:
        print(0, end = "")
    
quad(n, 0, 0)