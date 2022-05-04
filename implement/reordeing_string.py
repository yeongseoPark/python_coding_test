# 알파벳 대문자와 숫자 0~9로 이루어진 문자열이 입력으로 주어짐
# 이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤, 그 뒤 모든 숫자 더한 값 이어서 출력

s = input() # 1<=len(s)<=10000

str_list = []
int_list = []
for i in s:
    if ord(i) >= 65: # i.isalpha(): 문자열이 문자인지 확인-> 으로도 확인 가능 / .isdigit()
        str_list.append(i)
    else:
        int_list.append(int(i))
        #여기서 바로 sum_num += int(i)로 더해주는게 더 효율적일 듯!

str_list.sort()
str_collection = ''.join(s for s in str_list)
sum_num = sum(int_list)

result = str_collection+str(sum_num)
print(result)


