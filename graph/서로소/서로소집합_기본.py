# 특정 원소가 속한 집합을 찾기
def find_parent(parent,x):
    # # 루트 노드가 아니라면,루트 노드 찾을때까지 재귀적 호출 
    # # 최악의 경우 O(v)
    # if parent[x] != x:
    #     return find_parent(parent, parent[x])
    # return x
    
    # 경로 압축을 통해서 시간 복잡도 개선 
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x]) # 재귀 호출한 뒤, 부모테이블 값을 바로 갱신해줌
    return parent[x]

# 두 원소가 속한 집합 합치기 
def union_parent(parent, a, b):
    a = find_parent(parent, a) 
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int,input().split()) # 노드의 개수 v, 간선의 개수 e(합집합 연산의 개수)
parent = [0] * (v+1) # 부모테이블 초기화 

# 부모테이블 상에서, 부모를 자기자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# 간선 정보 입력받아 합집합 연산 수행
for i in range(e): # 최악의 경우 O(ve)
    a, b = map(int,input().split())
    union_parent(parent,a,b)

print('각 원소가 속한 집합: ', end='')
for i in range(1,v+1):
    print(find_parent(parent,i), end = ' ')
print()

print('부모 테이블: ', end='')
for i in range(1,v+1):
    print(parent[i], end=' ')