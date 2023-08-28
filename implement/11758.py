h, w = map(int, input().split())
block = list(map(int, input().split()))

amount = 0
for i in range(1, w-1):
    left_max = max(block[:i])
    right_max = max(block[i+1:])
    if left_max <= block[i] or right_max <= block[i]:
        pass
    else:
        amount += min(left_max, right_max) - block[i]
        
print(amount)
        
        