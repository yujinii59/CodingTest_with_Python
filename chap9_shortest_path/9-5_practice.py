import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split())

routes = list([] for _ in range(n + 1))
distances = [INF] * (n + 1)
for _ in range(m):
    x, y, z = map(int, input().split())
    routes[x].append((y, z))
    routes[y].append((x, z))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # (distance, to)
    distances[start] = 0
    while q:
        dist, to = heapq.heappop(q)
        if distances[to] < dist:
            continue

        length = len(routes[to])
        if length != 0:
            for after, distance in routes[to]:
                if distances[after] > dist + distance:
                    distances[after] = dist + distance
                    heapq.heappush(q, (dist + distance, after))
    return distances


distances = dijkstra(start=c)

cnt = -1
max_time = 0
for dist in distances:
    if dist < INF:
        cnt += 1
        max_time = max(max_time, dist)

print(cnt, max_time)