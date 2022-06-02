def solution(n, lost, reserve):
    count = n-len(lost)

    intersect = list(set(lost) & set(reserve)) # 도난 당한 학생이 여벌 있는 경우
    for i in intersect:
        count += 1
        reserve.remove(i)
        lost.remove(i)

    for i in lost:
        if i-1 in reserve:
            count += 1
            reserve.remove(i-1)
            continue
        elif i+1 in reserve:
            count += 1
            reserve.remove(i+1)
    return count

print(solution(3,[3],[1]))