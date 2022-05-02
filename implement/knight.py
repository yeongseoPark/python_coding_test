# 8 * 8 체스판
# L자형태 이동만 가능 / 체스판 밖에 못나감
# 수평 두칸 + 수직 한칸 이동 OR 수직 두칸 + 수평 한칸 이동 두가지만 가능
# 수평은 a~h 수직은 1~8
# 주어진 위치에 있을 때 이동할 수 있는 경우의 수는 몇개?

location = input()
row= int(location[1])
column = int(ord(location[0])-int(ord('a'))+1) #ord(): 문자열을 아스키코드로 반환
# ord('a')가 97이고, b는 98 c는 99 이렇게 하나씩 커짐
# 따라서 위의 식으로 a =>1 b =>2 이렇게 매칭

steps = [(-2,-1),(-2,1),(2,-1),(2,1),(-1,-2),(1,-2),(-1,2),(1,2)] #움직일  수 있는 경우의 수 

result = 0

for step in steps:
    next_row    = row+step[0] #steps가 LRUD의 dx,dy역할
    next_column = row+step[1]

    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8: # 이동가능하면
        result += 1 

print(result)