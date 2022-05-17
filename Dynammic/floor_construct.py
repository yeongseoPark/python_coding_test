# 가로 길이 n, 세로 길이 2 직사각형 바닥
# 이 바닥을 1X2의 덮개, 2X1의 덮개, 2X2의 덮개를 이용해 채우고자 한다.
# 이때 바닥을 채우는 모든 경우의 수 구하기

n = int(input()) # 1<=n<=1000

d = [0] * 1001 # dp 테이블 초기화 

d[1] = 1
d[2] = 3
for i in range(3,n+1):
    d[i] = (d[n-1] + 2 * d[n-2]) % 796796

print(d[n])
