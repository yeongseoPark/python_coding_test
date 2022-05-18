# n 개의 원소를 포함하고 있는 수열이 오름차순으로 정렬돼 있음
# 이 수열에서 x가 등장하는 횟수를 계산 / 하나도 등장하지 않는다면 -1
# {1,1,2,2,2,2,3} 일때 x=2 라면 4를 출력
# 이 문제는 시간복잡도 O(log N)으로 알고리즘 설계하지 않으면 시간 초과

def count_by_value(array,x):
    n = len(array)

    a = first(array, x, 0 , n-1) # x가 처음 등장한 인덱스 계산

    if a == None:  # 수열에 x가 존재하지 않는 경우
        return 0
    
    b = last(array,x, 0, n-1) # x가 마지막으로 등장한 인덱스 계산

    return b-a+1 # x의 개수를 반환

def first(array,target,start,end): # 첫 위치를 찾는 이진탐색 메서드
    if start > end:
        return None

    mid = (start+end) // 2

    if (mid == 0 or target > array[mid-1]) and array[mid] == target:
        # 해당 값을 갖는 원소들 중 가장 왼쪽에 있는 경우에만 인덱스 반환
        # mid가 맨 왼쪽에 있꺼나, mid이전 값이 target보다 작으면서, mid값은 target인경우
        return mid
    
    elif array[mid] >= target:
        # 중간 값보다 찾고자 하는 값이 적거나 같은 경우 왼쪽 확인
        return first(array, target, start, mid-1)
    
    else:
        # 중간 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        return first(array, target, mid+1, end)

def last(array,target, start,end):
    if start>end:
        return None
    
    mid = (start+end) // 2

    if (mid == n -1 or target < array[mid+1]) and array[mid] == target:
        #해당 값을 가지는 원소 중 가장 오른쪽에 있는 경우에만 인덱스 반환
        #first의 경우와 반대 
        return mid

    elif array[mid] > target:
        # 중간 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        return last(array, target, start, mid-1)
    
    else:
        # 중간 값보다 찾고자 하는 값이 크거나 같은 경우 오른쪽 확인
        return last(array, target, mid+1, end)


n,x = map(int,input().split())
array = list(map(int,input().split()))

count = count_by_value(array,x)

if count == 0:
    print(-1)
else:
    print(count)