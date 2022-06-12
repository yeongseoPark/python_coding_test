# # https://www.acmicpc.net/problem/2661

# 다시
def backtracking(idx):
    for i in range(1,(idx//2)+1):  
        if s[-i:] == s[-2*i:-i]: return -1 #나쁜순열인지 체크, 나쁜 순열이면 -1 리턴하며 종료
        # 뒤에서부터 범위 넓혀가며 최대 절반까지 체크

    if idx == n: # 백트래킹의 깊이가 n이고(idx를 하나씩 늘려가다 n이 됨), 종료조건 통과했다면 for문으로 정답 출력후 끝낸다
        for i in range(n): print(s[i], end='')
        return 0
    
    for i in range(1,4): # 1 , 2 , 3순으로 하나씩 이어보며 좋은수열인지 나쁜수열인지 확인
        s.append(i) 
        if backtracking(idx+1) == 0: #트리를 하나씩 이어가며 확인, n까지 좋은수열로 이어지면 밑의 pop실행 안하고 0 리턴하면 끝남
            return 0
        s.pop() # 만약 i를 더해 나쁜수열이 될 경우 방금 append해줬던 값을 지워줌
    
n = int(input())
s = []
backtracking(0)




