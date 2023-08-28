def draw_star(n, r, c, arr):
    if n == 3:
        arr[r][c] = '*'
        arr[r+1][c+1] = arr[r+1][c-1] = '*'
        arr[r+2][c-2:c+3] = ['*'] * 5
        return arr
    
    next_n = n // 2
    draw_star(next_n, r, c, arr)
    draw_star(next_n, r + next_n, c - next_n, arr)
    draw_star(next_n, r + next_n, c + next_n, arr)

N = int(input())
arr = [[' ' for _ in range(N * 2)] for _ in range(N)]

draw_star(N, 0 , N-1, arr)

for row in arr:
    print(''.join(row))