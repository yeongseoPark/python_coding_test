n = int(input())
arr = list(map(int,input().split()))

if n == 1:
    print(1)
    print(arr[0])
    
dp = [1] * n # dp[i] = 해당 위치에서의 LIS
dp_arr = [[arr[i]] for i in range(n)] # LIS를 담는 리스트

for i in range(1,n):
    for j in range(0,i):
        if arr[i] > arr[j]: # 전에 있는 무언가보다 크면
            if dp[i] < dp[j] + 1: # 만약 전의 LIS에 날 더하는게 더 큰 결과를 만들면
                dp[i] = dp[j] + 1
                dp_arr[i] = dp_arr[j][:] + [arr[i]] # LIS리스트 갱신
                
max_val = max(dp)
max_idx = dp.index(max_val)
        
print(max_val)
print(" ".join(map(str, dp_arr[max_idx])))    
                
                
                


