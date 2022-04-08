n, m = map(int, input().split())

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


parent = [i for i in range(n + 1)]
routes = []
total_cost = 0
max_cost = 0
for _ in range(m):
    a, b, cost = map(int, input().split())
    routes.append((cost, a, b))

routes.sort()

for cost, a, b in routes:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        total_cost += cost
        max_cost = max(cost, max_cost)

print(total_cost - max_cost)
