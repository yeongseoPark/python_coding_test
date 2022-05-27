def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int,input().split())
parent = [0] * (v+1)

edges = [] # 모든 간선
result = 0 # 최종 비용

for i in range(1,v+1):
    parent[i] = i # 자기 자신으로 부모 초기화

for _ in range(e):
    a,b ,cost = map(int,input().split())
    edges.append((cost,a,b))  #비용순 정렬을 위해 튜플의 첫 원소 비용으로 설정

edges.sort()

for edge in edges:
    cost , a, b = edge

    if find_parent(parent, a) != find_parent(parent,b): #루트가 다른경우(사이클 발생하지 않는 경우)에만 집합에 포함
        union_parent(parent, a, b)
        result += cost

print(result)