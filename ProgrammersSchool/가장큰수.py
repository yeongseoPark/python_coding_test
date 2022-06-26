


# def solution(numbers):
#     # if len(set(numbers)) == 1 and  set(numbers[0]) == 0:
#     #     return "0"
#     numbers = list(map(str,numbers))
#     numbers.sort(key = lambda x: x*3, reverse=True) 
#     # 최대 자리수 3자릿수를 활용
#     # 문자열의 정렬은 첫번째 인덱스부터 아스키코드값으로 비교함
#     # (문자열의 int값의 크기로 비교 x)
#     # 첫번째 인덱스가 동일하다면 다음 인덱스로비교 ~
#     strl = int("".join(numbers))
#     return str(strl)
# print(solution([3, 30, 34, 5, 9]))

def solution(numbers):
    numbers = list(map(str,numbers))
    
    max_leng = max(numbers, key=len)
    
    strr = ""
    numbers.sort(key = lambda x: x*max_leng) # 문자열 정렬이기에, 3이 30보다 뒤에(크게)정렬되기위해 자릿수를     max_leng 이상으로 키워준다
    
    while numbers:
        a = numbers.pop()
        strr += a
    
    return strr
print(solution([3, 30, 34, 5, 9]))