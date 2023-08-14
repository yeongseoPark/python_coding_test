n, m = map(int, input().split())

p = [i for i in range(n+1)]
rank = [0] * (n+1) # 각 원소의 높이 저장

# Union by Rank : 높이가 낮은 트리를 높이가 높은 트리의 아래에 붙임
# 높이가 더 높은쪽이 root
def union(a, b):
    rootA = find(a)
    rootB = find(b)

    if rootA != rootB:
        if rank[rootA] > rank[rootB]:
            p[rootB] = rootA
        else:
            p[rootA] = rootB
            if rank[rootA] == rank[rootB]: # 만약 높이가 같다면 합친 후, rootB의 높이 += 1
                rank[rootB] += 1

"""
이를 통해 트리의 높이가 불필요하게 길어지는 것 방지 -> 트리의 높이에 비례하는 find연산속도 빨라짐
"""


# 경로압축 : 루트에 모든 노드를 연결, find하며 만난 모든 값의 부모를 root로.
# 따라서 find호출시 경로가 훨씬 짧아짐, 상수시간
def find(x):
    if x != p[x]:
        p[x] = find(p[x])
    return p[x]

    """_느린버전 : 각 원소가 상위 노드에 연결됨_
    def find(x):
        while x != p[x]:
            x = p[x]
        return x
    """

for _ in range(m):
    code, a, b = map(int, input().split())

    if code == 0:
        union(a, b)

    else:
        if find(a) == find(b):
            print("yes")
        else:
            print("no")