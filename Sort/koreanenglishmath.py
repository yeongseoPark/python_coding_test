# https://www.acmicpc.net/problem/10825

# 1. 국어 점수가 감소하는 순서
# 2. 국어 점수 같으면 영어 점수가 증가하는 순서
# 3. 국어와 영어 점수 같으면 수학 점수 감소하는 순서
# 4. 모두 같으면 이름이 사전순으로 증가하는 순서(아스키 코드에서 대문자는 소문자보다 작으므로 사전순으로 앞에 온다)


# 답안 -> 튜플 구성하는 원소의 순서에 맞게 정렬되는 특성 활용

n = int(input())
students = []

for i in range(n):
    students.append(input().split()) # 리스트 안에 리스트로 담아줌

students.sort(key=lambda x:(-int(x[1]), int(x[2]), -int(x[3]), x[0]) )
    # 튜플의 원소의 순서에 맞게 정렬, -붙이면 내림차순

for student in students:
    print(student[0])


# 2 틀린풀이 : 국어가 "다" 같은 경우 "다" 영어로 정렬~ 이런 식으로 됨
# 세개 중 국어 점수가 두개 같으면, 그 둘은 영어로 정렬. 이 논리가 맞음
n = int(input())

lst = []
for i in range(n):
    input_data = input().split()
    lst.append([str(input_data[0]), int(input_data[1]), int(input_data[2]),int(input_data[3])])

sorted_lst = sorted(lst, key=lambda korean: korean[1],reverse=True) #국어 내림차순

if sorted_lst == lst: 
    sorted_lst = sorted(lst, key=lambda english: english[2]) # 영어 오름차순

if sorted_lst == lst:
    sorted_lst = sorted(lst, key=lambda math: math[3], reverse= True) # 수학 내림차순 

if sorted_lst == lst:
    sorted_lst = sorted(lst, key=lambda name: name[0]) # 이름 사전순 증가

for i in sorted_lst:
    print(i[0])