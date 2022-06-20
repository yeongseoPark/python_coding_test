
def solution(arr):
    answer= []
    no_duple = 0
    for i in set(arr):
        times = arr.count(i)
     
        if times == 1:
            no_duple += 1
            if no_duple == len(set(arr)):
                answer.append(-1)

        if times > 1:
            answer.append(times)
    
    return answer

print(solution([3, 5, 7, 9, 1]))