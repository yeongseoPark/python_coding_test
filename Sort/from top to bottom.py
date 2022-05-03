# 무작위로 수가 나열된 수열을, 큰 수부터 작은 수의 순서로 정렬
# 내림차순 정렬

n = int(input()) # 수열에 속해있는 수의 개수 n
lst = []
for i in range(n):
    lst.append(int(input()))

sorted_lst = sorted(lst, reverse=True) 
# 별도의 정렬된 리스트가 반환되기에
# 다른 변수에 담아주기

for i in sorted_lst:
    print(i, end = ' ')