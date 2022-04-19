from collections import deque

n = int(input())

courses = [[] for _ in range(n + 1)]
costs = [0] * (n + 1)
degree = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    inputs = list(map(int, input().split()))
    costs[i] = inputs[0]
    for course in inputs[1:]:
        if course != -1:
            degree[i] += 1
            courses[course].append(i)

times = [0] * (n + 1)
time = 0
q = deque()
for i in range(1, n + 1):
    if degree[i] == 0:
        q.append(i)
        times[i] = time + costs[i]

while q:
    node = q.popleft()
    time = times[node]
    for course in courses[node]:
        degree[course] -= 1

        if degree[course] == 0:
            q.append(course)
            times[course] = time + costs[course]

for course_time in times[1:]:
    print(course_time)

