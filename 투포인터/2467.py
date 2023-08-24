n = int(input())
arr = list(map(int, input().split()))

left = 0
right = n-1
zero = 3000000001
ans_left = 0
ans_right = 0

while left != right:
    if arr[right] + arr[left] > 0:
        if abs(arr[right] + arr[left] - 0) < abs(zero):
            zero = abs(arr[right] + arr[left] - 0)
            ans_left = left
            ans_right = right
            
        right -= 1
                
    elif arr[right] + arr[left] < 0:
        if abs(arr[right] + arr[left] - 0) < abs(zero):
            zero = abs(arr[right] + arr[left] - 0)
            ans_left = left
            ans_right = right
            
        left += 1
    
    else:
        print(arr[left], arr[right])
        exit()

print(arr[ans_left], arr[ans_right])