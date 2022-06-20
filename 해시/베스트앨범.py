def solution(genres, plays):
    answer = []

    # { 장르 : 총 재생횟수}
    playsdict = {}

    # { 장르 : [(플레이횟수, 고유번호)]}
    dict = {}

    for i in range(len(genres)): 
        genre = genres[i]
        play  = plays[i]
        playsdict[genre] = playsdict.get(genre,0) + play  # 0기본값으로 시작해서 play만큼 더해나감
        # get(키,디폴트값) 
        # 딕셔너리 안에 찾으려는 key값이 없을 경우, 미리 정해둔 디폴트 값을 대신 가져오게 하기
        dict[genre] = dict.get(genre, []) + [(play,i)] # 빈리스트로 시작해서 (플레이횟수, 고유번호) 더해나감

    genresort = sorted(playsdict.items(), key=lambda x: x[1], reverse=True)
    # [(장르, 재생횟수),(장르,재생횟수)...] 에서 재생횟수를 기준으로 내림차순 정렬

    for (genre, total) in genresort:
        dict[genre] = sorted(dict[genre], key=lambda x: (-x[0], x[1]))  # 람다에 정렬기준 두개 넘김
        # 플레이횟수(0번인덱스) 내림차순, 고유번호 오름차순으로 정렬하기
        answer += [idx for (play,idx) in dict[genre][:2]]
        # 장르내에서 두개까지 뽑아서 answer에 더하기
    
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]))