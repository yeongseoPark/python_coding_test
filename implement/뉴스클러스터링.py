import re

def solution(str1, str2): # 내풀이
    str1_pairs = [] # 각각 집합 만듬
    for i in range(len(str1)-1): 
        if ((ord(str1[i]) <= 90 and ord(str1[i]) >= 65) or (ord(str1[i]) >= 97 and ord(str1[i]) <= 122)) and ((ord(str1[i+1]) <= 90 and ord(str1[i+1]) >= 65) or (ord(str1[i+1]) >= 97 and ord(str1[i+1]) <= 122)) :
            one = str1[i].lower()
            two = str1[i+1].lower()
            str1_pairs.append(one+two)
    str2_pairs = []
    for i in range(len(str2)-1): 
        if ((ord(str2[i]) <= 90 and ord(str2[i]) >= 65) or (ord(str2[i]) >= 97 and ord(str2[i]) <= 122)) and ((ord(str2[i+1]) <= 90 and ord(str2[i+1]) >= 65) or (ord(str2[i+1]) >= 97 and ord(str2[i+1]) <= 122)) :
            one = str2[i].lower()
            two = str2[i+1].lower()
            str2_pairs.append(one+two)
    
    if str1_pairs == [] and str2_pairs == []: # 둘다 공집합일 경우 예외처리 
        return 65536
    
    print(str1_pairs)
    print(str2_pairs)
    
    kyo = []
    for i in str1_pairs:
        if i in str2_pairs and i not in kyo:
            tmp = []
            tmp.append(str1_pairs.count(i))
            tmp.append(str2_pairs.count(i))
            for j in range(min(tmp)):
                kyo.append(i)
                
            
    print(kyo)
    
    hab     = []
    hab_tmp = []
    for i in str1_pairs:
        hab_tmp.append(i)
    for i in str2_pairs:
        hab_tmp.append(i)
    
    for i in hab_tmp:
        if hab_tmp.count(i) > 1 and i not in hab:
            one_count = str1_pairs.count(i)
            two_count = str2_pairs.count(i)
            maxy = max(one_count,two_count)
            
            for j in range(maxy):
                hab.append(i)
        elif hab_tmp.count(i) == 1 and i not in hab:
            hab.append(i)
            
    print(hab)
    
    return int((len(kyo) / len(hab))*65536)


def solution(str1, str2):
    # findall : 정규식과 매치되는 모든 문자열을 리스트 형식으로 리턴 / re.findall(r'패턴문자열', '문자열')
    # ^[a-zA-Z]+$ : ^ - 시작 | [a-zA-Z] - 영문자 | + - 대괄호안 문자가 한개이상 | $ 문자열의 끝 지정, 문자열의 끝이 앞의 정규식과 같다
    str1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if re.findall('^[a-zA-Z]+$', str1[i:i+2])] 
    str2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if re.findall('^[a-zA-Z]+$', str2[i:i+2])]

    hab = set(str1) | set(str2)
    kyo = set(str1) & set(str2)

    if len(hab) == 0: # 둘다 공집합이면
        return 65536
    
    # 다중집합 조건 처리    
    gyo_sum = sum([min(str1.count(g),str2.count(g)) for g in kyo])
    hab_sum = sum([max(str1.count(h),str2.count(h)) for h in hab])

    return int((gyo_sum/hab_sum)*65536)


