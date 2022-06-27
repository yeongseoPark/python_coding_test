def solution(s):
    s = s[2:len(s)-2]
    arr = s.split("},{")
    if len(arr) == 1:
        return list(map(int,arr))
    result = []
    for i in arr:
        if len(i) == 1:
            result.append([int(i)])
        else:
            splitted = list(i.split(","))
            result.append(list(map(int, splitted)))
    answer = []
    result.sort(key=len)
    
    
    for i in range(len(result)-1):
        if len(result[i]) == 1:
            answer.append(result[i][0])
            
        new = list(result[i+1])
        for j in range(len(result[i])):
            new.remove(result[i][j])
        answer.append(new[0])
        
    return answer 
        

        
    
solution("{{123}}")