
# def solution(phone_book): # 답보고 품
#     hash_map = {phone_number: 1 for phone_number in phone_book} # 각 전화번호:1 인 해시맵 만듬

#     for phone_number in phone_book: # 전화번호부에 있는 모든 전화번호 loop [ 0107415, 010]
#         jubdoo = ""                 # jubdoo라는 문자열 만들고 
#         for num in phone_number:    # 전화번호 한자리씩 jubdoo에 더해준다 
#             jubdoo += num     

#             if jubdoo in hash_map and jubdoo != phone_number: # 위 과정중에 만약 jubdoo가 해시맵의 key들 중하나(다른 전화번호)이고,
#                 # 그게 지금 loop도는 번호가 아니라면, 현 전화번호에 접두어가 되는 다른 번호가 존재하는 것이므로
#                 # 딕셔너리의 in은 key에 한해 동작
#                 # 굳이 hash_map.keys()로 바꿀필요x
#                 return False # False 리턴
    
#     return True 

def solution(phone_book):
    phone_book.sort() # 숫자값 정렬x, 앞자리에서부터 아스키코드값으로 정렬되기에
    # 앞이 같으면 연이어서 정렬됨
    
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    
    return True

solution(["12","123","1235","567","88"]	)
        
    
    
# def solution(phone_book): 효율성 3,4 통과 못함
#     # min_len = min([len(i) for i in phone_book]) # 가장 짧은 길이
#     # ..를 구할필요 없구나... 가장 짧지 않아도 더 긴 문자열의 접두사 될 수 있음
#     # mins = [i for i in phone_book if len(i) == min_len]
    
#     phone_book.sort()
    
#     for i in phone_book: 
#         for j in phone_book:
#             jubdoo = ""            
#             for k in j: 
#                 jubdoo += k
#                 if jubdoo == i and j != i:
#                     return False
    
#     return True


# def solution(phone_book): 풀이2 45.8점: 
# 가장 짧은 전화번호들 추린후, 딕셔너리에 전화번호의 키:출현횟수로 넣어준 이후, 
# 다른 번호들 돌면서 -= 씩해주어 모두 키:0  되는지 확인 
#     len_list = [len(i) for i in phone_book]
#     min_len = min(len_list) 
    
#     min_values = [i for i in phone_book if len(i) == min_len]
    
#     for i in min_values:
#         phone_book.remove(i)
    
#     min_value_dics = []
#     for i in min_values:
#         min_value_dics.append({j: i.count(j) for j in i})
    
#     for i in min_value_dics:
#         for j in phone_book:
#             for k in j:
#                 if i[k] != None:
#                     i[k] -= 1
#                 if len(set(i.values())) == 1 and list(set(i.values()))[0] == 0:
#                     return False
#     return True

        
    


# def solution(phone_book): # 첫 풀이 20.8점
#     len_list = [len(i) for i in phone_book]
#     min_len = min(len_list)

#     min_values = [i for i in phone_book if len(i) == min_len]

#     for i in phone_book: # 각 전화번호 
#         for j in min_values: # 가장 길이가 짧은 아이들 
#             for k in range(1,min_len): # min_len만큼 각 전화번호의 앞 확인하며 접두사되는지 확인
#                 if j[:k] == i[k]:
#                     return False
    
#     return True


