n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

max_p = arr[0]
max_tmp = [0] * 3
min_p = arr[0]
min_tmp = [0] * 3

for i in range(1, n):
    for j in range(3):
        if j == 0:
            max_tmp[j] = max(max_p[j], max_p[j+1]) + arr[i][j]
            min_tmp[j] = min(min_p[j], min_p[j+1]) + arr[i][j]
        elif j == 1:
            max_tmp[j] = max(max_p[j-1] , max_p[j], max_p[j+1]) + arr[i][j]
            min_tmp[j] = min(min_p[j-1] , min_p[j], min_p[j+1]) + arr[i][j]

        elif j == 2:
            max_tmp[j] = max(max_p[j-1], max_p[j]) + arr[i][j]
            min_tmp[j] = min(min_p[j-1], min_p[j]) + arr[i][j]
    max_p = max_tmp[:] # 주소값이 아니라 값을 하드카피 해줘야함
    min_p = min_tmp[:]

print(str(max(max_p)) + " " + str(min(min_p)))
