# https://programmers.co.kr/learn/courses/30/lessons/49993

def solution(skill, skill_trees):
    possible_tree = 0
    for tree in skill_trees: 
        relevant_a = []
        for a in tree:
            if a in skill:
                relevant_a.append(a) # 스킬트리에서 선행스킬들과 관련있는 것 append
                 
        if len(relevant_a) == 0: # 만약에 선행스킬들과 아무 상관없는 애들만 있다면.. 
            # relevant_a == None 으로 했을때는 []가 조건에 안걸림.빈 리스트와 다르게 None이라는 별도의 객체가 있음
            possible_tree += 1
            continue
        
        #이제 releveant_a가 skill과 같은 순서인지 확인하면 됨: skill의 처음부터 시작해야하고, 중간에 빈 것 있으면 안됨
        skill_list = list(skill)
        skill_list_for_compare = skill_list[:len(relevant_a)]
        if skill_list_for_compare == relevant_a:
            possible_tree += 1
    
    return possible_tree


    
print(solution("CBD" ["C", "D", "CB", "BDA"]))
    