n = int(input())
rope = []
for i in range(n):
    rope.append(int(input()))

rope.sort(reverse=True)

max_val = -1
for i in range(len(rope)):
    max_val = max(max_val, rope[i] * (i+1))

print(max_val)