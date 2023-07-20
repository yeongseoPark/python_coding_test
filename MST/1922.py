n = int(input())
m = int(input())

edges = []
# a,b사이를 연결하는 간선 여러개 있을 수 있기 때문에 최소값을 얻기 위해서 edges_dict 사용
edges_dict = {}
for _ in range(m):
    a, b, c = map(int, input().split())
    if edges_dict.get((a,b)) is not None: 
        if c < edges_dict[(a,b)]:
            edges_dict[(a,b)] = c
    else:
        edges_dict[(a,b)] = c 

for a,b in edges_dict.keys():
    edges.append((a,b, edges_dict[(a,b)]))

edges.sort(key = lambda x : x[2])

all_cost = 0
count = 0 

set_all_nodes = [i for i in range(n+1)]

def find(x):
    while x != set_all_nodes[x]:
        x = set_all_nodes[x]
    return x 

for a, b, cost in edges:
    if count == n-1:
        break 
    if find(a) != find(b):
        all_cost += cost
        count += 1 
        set_all_nodes[find(b)] = find(a) # union
        
print(all_cost)   