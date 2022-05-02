# #1
n=1260
count =0

coin_list=[500,100,50,10]

for i in coin_list: #O(코인종류)
    count_i = n//i
    n= n-(count_i * i)
    count += count_i

print(count)

# 2

n= 1260
count =0

coin_list=[500,100,50,10]

for i in coin_list: #O(코인종류)
    count += n//i
    n %= i # n = n%i(나머지)

print(count)