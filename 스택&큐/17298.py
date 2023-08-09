n = int(input())
arr = list(map(int, input().split()))

answer = [-1] * n
stack = [0]

for i in range(1, n):
    while stack and arr[stack[-1]] < arr[i]:
        answer[stack[-1]] = arr[i]
        stack.pop()

    stack.append(i)

print(*answer)