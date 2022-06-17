# def solution(answers): # 50점....
#     one = [1,2,3,4,5]
#     two = [2,1,2,3,2,4,2,5]
#     three = [3,3,1,1,2,2,4,4,5,5]
#     score = 



def solution(answers): # 50점....
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    
    compare_one = one*(len(answers)//len(one)) + one[:len(answers)%len(one)]
    one_count = 0
    for i in range(len(answers)):
        if answers[i] == compare_one[i]:
            one_count += 1
    
    compare_two = two*(len(answers)//len(two)) + two[:len(answers)%len(two)]
    two_count = 0
    for i in range(len(answers)):
        if answers[i] == compare_two[i]:
            two_count += 1
            
    compare_three = three*(len(answers)//len(three)) + three[:len(answers)%len(three)]
    three_count = 0
    for i in range(len(answers)):
        if answers[i] == compare_three[i]:
            three_count += 1
    
    counts = [one_count,two_count,three_count]
    result = [[1,one_count],[2,two_count],[3,three_count]]
    standard = max(counts)
    for i in result[:]: # for문이 도는 result는 원본이기에, remove를 사용할시 원본이 손상돼 완전한
        # for문이 돌지 않는다. 따라서 result[:]의 형식으로 복사본을 활용한다
        if i[1] < standard:
            result.remove(i)

    real = []
    for i in result:
        real.append(i[0])
    
    sorted(real)
    return real

solution([1,2,3,4,5])