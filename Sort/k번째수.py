def solution(array, commands):
    answer = []
    for i in commands:
        new = array[i[0]-1:i[1]]
        new.sort()
        answer.append(new[i[2]-1])
    return answer

solution([1, 5, 2, 6, 3, 7, 4],	[[2, 5, 3], [4, 4, 1], [1, 7, 3]])