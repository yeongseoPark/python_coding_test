# https://programmers.co.kr/learn/courses/30/lessons/12980


# k칸 점프시 점프한 칸만큼 건전지 사용
# 순간이동 = 현재까지 온 거리 X 2 
# 점프 이동 최소화 목적
def solution(n):
    ans = 0
    while n>0:
        ans += n % 2
        n //= 2
    return ans
# top-down으로 접근
# 2로 나눠떨어지는 곳은 순간이동으로 갈수 있다
# 나눠떨어지지 않으면 그 나머지만큼은 점프를 해야하기에, 에너지에 n%2를 더해준다
print(solution(7))
        

