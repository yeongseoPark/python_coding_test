# n명의 학생 정보
# 학생 정보는 학생 이름과 학생 성적으로 구분됨
# 성적이 낮은 순서대로 학생 이름 출력
# 학생의 정보는 최대 100000개 

n = int(input()) # 학생의 수 n
lst = []
for i in range(n):
    # lst.append(tuple(map(str,input().split()))) # 첨엔 이렇게 한번에 튜플로 묶었는데
    # 이렇게 말고 점수는 int로 받아야 함
    input_data = input().split() # ["길동","95"] 이렇게 리스트로 묶임
    lst.append((input_data[0], int(input_data[1]))) # 점수 int로 변환

# def setting(data):
#     return data[1]
# 람다로 처리하는게 훨씬 깔끔함

sorted_list = sorted(lst, key=lambda grade: grade[1]) 
#lambda 매개변수: 반환값 식
for i in sorted_list:
    print(i[0], end=' ')

# 최대 100000개 입력되기에 최악의 경우에도 O(n log n) 보장하는 알고리즘 or o(n)보장되는 계수 정렬 사용
