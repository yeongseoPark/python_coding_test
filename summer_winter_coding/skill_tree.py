# https://programmers.co.kr/learn/courses/30/lessons/49993

def solution(skill, skill_trees):
    possible_tree = 0
    for tree in skill_trees:
        relevant_a = []
        for a in tree:
            if a in skill:
                relevant_a.append(a)
                 
        if len(relevant_a) == 0: # 만약에 선행스킬들과 아무 상관없는 애들만 있다면 
            # relevant_a == None 으로 했을때는 []가 조건에 안걸림.빈 리스트와 다르게 None이라는 별도의 객체가 있음
            possible_tree += 1
            continue
        
        #이제 releveant_a가 skill과 같은 순서인지 확인하면 됨ㅠ -> 단순 같은 순서ㄴㄴ 중간에 빈 것 없어야
        skill_list = list(skill)
        for i in skill_list:
            if i not in relevant_a:
                skill_list.remove(i)
        
        length = len(skill_list)
        array_for_compare = skill_list + relevant_a
        if array_for_compare[:length] == array_for_compare[length:] and array_for_compare[length] == skill[0]:
            possible_tree += 1
    
    return possible_tree


    
print(solution("CBD" ["C", "D", "CB", "BDA"]))
    