n, m = map(int, input().split())

operations = []
for _ in range(m):
    oper, a, b = map(int, input().split())
    operations.append((oper, a, b))


def find_team(teams, student):
    if teams[student] != student:
        teams[student] = find_team(teams, teams[student])
    return teams[student]


def union_team(teams, student1, student2):
    team1 = find_team(teams, student1)
    team2 = find_team(teams, student2)
    if team1 < team2:
        teams[team2] = team1
    else:
        teams[team1] = team2


teams = [i for i in range(n + 1)]

for oper, a, b in operations:
    if oper == 0:
        union_team(teams, a, b)
    else:
        if find_team(teams, a) == find_team(teams, b):
            print('YES')
        else:
            print('NO')
