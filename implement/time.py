# n입력되면 0시 00분 00초 ~ n시 59분 59초 사이의 모든 시각 중, 3이 하나라도 포함되는 모든 경우의 수 구하기
# 완전 탐색 - 모든 경우의 수 다 탐색하기

n = int(input())

count = 0
for i in range(n+1):
    for j in range(60):
        for h in range(60):
            if '3' in str(i) + str(j) + str(h):
                count += 1
# 시간 복잡도 매우 높음
# 따라서 탐색할 데이터 100만개 이하일때 사용하면 적절
print(count)