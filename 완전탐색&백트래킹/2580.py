def is_possible(x, y, num, board):
    # 같은 행에 해당 숫자가 있는지 확인
    for i in range(9):
        if board[x][i] == num:
            return False
            
    # 같은 열에 해당 숫자가 있는지 확인
    for i in range(9):
        if board[i][y] == num:
            return False
            
    # 3x3 구역에 해당 숫자가 있는지 확인
    sx, sy = (x//3)*3, (y//3)*3
    for i in range(3):
        for j in range(3):
            if board[sx+i][sy+j] == num:
                return False
                
    return True


def solve(board):
    for x in range(9):
        for y in range(9):
            # 빈 칸인 경우
            if board[x][y] == 0:
                for num in range(1, 10): # 1부터 9까지 숫자를 넣어봄
                    if is_possible(x, y, num, board): # 가능한 숫자일 때
                        board[x][y] = num
                        if solve(board):
                            return True
                        # 여기까지 왔으면 해당 숫자로는 해결 안됨. 다시 0으로 변경
                        board[x][y] = 0
                # 1~9까지 모든 숫자를 넣어봤는데 해결 안됨. 백트래킹
                return False

    return True # 모든 칸이 채워진 경우


board = [list(map(int, input().split())) for _ in range(9)]
solve(board)
for row in board:
    print(' '.join(map(str, row)))
