# 배열로 주어진 수 m번 더하여 가장 큰 수를 만드는 법칙
# 배열의 특정한 인덱스에 해당하는 수가 "연속해서 k번" 초과해서 더해질 수 없음
# 서로 다른 인덱스에 해당하는 수가 같더라도, 다른 것으로 간주
# 배열의 크기 N, 숫자 더해지는 횟수 M, 그리고 연속 제한K



n,m,k = map(int,input("insert N,M,K").split()) 
numbers = list(map(int,input("insert numbers").split()))

numbers.sort() # 오름차순 정렬
first  = numbers[n-1] # 다른 인덱스, 같은 값 있다면
second = numbers[n-2] # 이 과정에서 자연스럽게 둘다 선택됨

# 1
# result = 0

# while True:
#     for i in range(k): #젤 큰수 k번 더하기
#         if m==0: 
#             break # m번더하면 탈출
#         result += first
#         m -= 1 # 더할때마다 m하나씩 차감
#     if m ==0: 
#         break
#     result += second # 두번째 큰수 한번 더하기 
#     m -= 1

# print(result)

# 2
# 반복되는 수열의 길이 k+1 , k=3일때  (first,first,first,second)
first_count = int((m / (k+1)) * k + m % (k+1))
# m(횟수)를 k+1로 나눈 값(수열의 반복횟수)* k 에
# m이 k+1로 나눠떨어지지 않을 때, 그것의 나머지 까지가 
# 첫번째 값이 더해지는 수

secound_count = m-first_count

result = 0
result += first*first_count
result += second*secound_count
print(result)


