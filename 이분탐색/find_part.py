import sys
# 가게에는 n 개의 부품. 각 부품에는 정수형의 고유 번호 존재
# 손님이 m개 종류의 부품을 대량으로 구매하겠다고 함
# 손님이 문의한 m개 종류가 모두 있는지 확인하는 프로그램
# 각 부품이 존재하면 yes 없으면 no 출력 

n = int(input()) # 1 <= n <= 1000000
array = list(map(int,sys.stdin.readline().split()))
array.sort() # 시간복잡도 O(n * log N) -> log2백만은 약 20 이므로 최대 연산 2000만

m = int(input()) # 1 <= m <= 100000
find_array = list(map(int,sys.stdin.readline().split()))

def binary_search(array, target, start, end): # 최악의 경우 시간복잡도 O(m X logN) : log2십만은 16이므로 16*10만 = 최대연산 약 170만
    if start > end:
        return None
    
    mid = (start+end) // 2

    if array[mid] > target:
        return binary_search(array, target, start, mid-1)
    elif array[mid] < target:
        return binary_search(array, target, mid+1, end)
    else:
        return mid

for i in range(m):
    result = binary_search(array, find_array[i], 0, n-1)
    if result == None:
        print("no", end = " ")
    else:
        print("yes", end=" ")


# 계수 정렬을 이용한 문제풀이

n = int(input()) # 가게 부품의 개수
array = [0] * 1000001 # 모든 원소의 번호(1~100만)를 포함할 수 있는 크기의 리스트를 만듬

for i in input().split():
    array[int(i)] = 1
# 가게 부품의 번호에 해당하는 인덱스에 1을 기록

m = int(input()) # 손님이 요청한 부품 개수

x = list(map(int,input().split())) # 손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력

for i in x:
    if array[i] == 1:
        print('yes', end=" ")
    else:
        print("no", end=" ")

