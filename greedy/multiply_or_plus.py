# 각 자리가 숫자로만(0~9) 이루어진 문자열 s
# 왼쪽에서 오른쪽으로 하나씩 모든 숫자 확인하며
# 숫자 사이에 '*' 또는 '+' 연산자 넣어 결과적으로 만들어질 수 있는 가장 큰 수 구하기
# 단, +보다 * 먼저 계산하지 않고, 왼쪽에서부터 순서대로 계산 이루어짐
# 만들어 질 수 있는 가장 큰 수는 항상 20억 이하의 정수가 되도록 입력 주어짐

s = input() # 1<=s<=20

# 풀이 2: 두 수에 대해서 연산을 수행할 때, 두 수 중 하나라도 1이하인 경우에 더하고, 아니면 곱한다

result = int(s[0])
for i in range(1,len(s)):
    if result <= 1:
        result += int(s[i])
    else:
        if s[i] <= 1:
            result += int(s[i])
        else:
            result *= int(s[i])

print(result)


# 3 답안
result = int(s[0])
for i in range(1,len(s)):
    num = int(s[i])
    if num <=1 or result <= 1:
        result += num
    else:
        result *= num
print(result)


# 풀이: 1이 있는 경우에 더하기 수행이 더 크다는 것 반영x
s_list = list(s)
# 0있으면 걍 빼고 계산해주면 됨
if "0" in s:
    s_list.remove("0")
    result = int(s_list[0])
    for i in s_list[1:]:
        result *= int(i)

else:
    result = int(s_list[0])
    for i in s_list[1:]:
        result *= int(i)

print(result)





