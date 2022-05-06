# https://programmers.co.kr/learn/courses/30/lessons/42889

def solution(n, stages):
    rates = {} # 각 스테이지에 해당하는 실패율 담김
    for i in range(1,n+2):
        if stages.count(i) + len([y for y in stages if y > i]) == 0:
            fail_rate = 0
        else:
            fail_rate = stages.count(i) / (len([y for y in stages if y > i])+stages.count(i))
        rates[i] = fail_rate
    del rates[n+1]
    rates = sorted(rates.items(), key=lambda x:x[1], reverse=True) #dict에 값을 키로 sorted 쓰면 (키,값) 담긴 리스트로 변환
    # list.sort()는 리스트에만 사용 가능하지만, sorted는 모든 이터러블에 가능
    results = [i[0] for i in rates]
    return results


solution(4,[4,4,4,4,4])