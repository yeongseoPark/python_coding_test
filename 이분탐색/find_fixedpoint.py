# 고정점: 수열의 원소 중 그 값이 인덱스와 동일한 원소
# 하나의 수열이 n개의 서로 다른 원소를 포함하고 있으며, 모든 원소가 오름차순으로 정렬
# 이때 이 수열에 고정점이 있다면, 고정점을 출력하는 프로그램을 작성
# 고정점은 최대 1개만 존재, 고정점이 없다면 -1 출력
# 시간복잡도 O(log N)으로 알고리즘을 설계할 것

def binary(target, array, start, end):
    if start > end:
        return -1

    mid = (start+end) // 2 

    if array[mid] == target and (mid == target):  
        return mid
    
    elif array[mid] < target:
        return binary(target,array,mid+1,end)
    
    else:
        return binary(target,array,start,mid-1)

n = int(input()) # 1<=n<=1000000
array = list(map(int,input().split()))


count = 1
for i in array:
    a = binary(i,array,0,n-1)
    count += 1
    if a != -1:
        print(a)
        break
    if count == len(array):
        print(-1)

# 책 답안
def binary_search(array,start,end): # target을 인자로 받지 않음
    if start>end:
        return None

    mid = (start+end)//2

    if array[mid] == mid: # 인덱스 값인 mid 자체를 target으로 둠
        return mid 
    
    elif array[mid] > mid:
        return binary_search(array,start,mid-1)
    else:
        return binary_search(array,mid+1,end)
    
    n = int(input())
    array = list(map(int,input().split()))

    index = binary_search(array,0,n-1)
     # mid가 계속 옮겨가며 인덱스와 값이 일치하는지 확인하기에
     # 위에서처럼 for문 돌릴필요없음

    if index == None:
        print(-1)
    else:
        print(index)