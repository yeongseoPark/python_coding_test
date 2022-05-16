import sys


def binary_search(array, target, start, end):
    while end >= start:
        mid = (start + end) // 2

        if array[mid] > target:
            end = mid-1
        
        elif array[mid] < target:
            start = mid + 1

        else:
            return mid
    return None
        
n, target = map(int,sys.stdin.readline().split())

array = list(map(int,sys.stdin.readline().split()))

result = binary_search(array, target, 0 , n-1)

if result == None:
    print("찾으려는 값이 없습니다")
else:
    print(result+1)