n, m = map(int, input().split())
INF = int(10e9)

routes = list([INF] * (n + 1) for _ in range(n + 1))

for _ in range(m):
    connect = list(map(int, input().split()))
    if connect[0] != connect[1]:
        routes[connect[0]][connect[1]] = routes[connect[1]][connect[0]] = 1

for i in range(n + 1):
    routes[i][i] = 0

x, k = map(int, input().split())

for i, route in enumerate(routes):
    for j, move in enumerate(route):
        if move != 0:
            for k in range(n + 1):
                routes[i][k] = min(routes[i][k], move + routes[j][k])

move_count = routes[1][k] + routes[k][x]

if move_count >= INF:
    print(-1)
else:
    print(move_count)
