n, m = map(int, input('맵 크기를 입력해주세요 : ').split())
row, col, direction = map(int, input('캐릭터의 위치와 바라보는 방향을 입력해주세요 : ').split())

map_status = list()
map_check = list([0] * m for _ in range(n))
direct_info = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
for i in range(n):
    status = list(map(int,input(f'{i + 1}행의 공간의 상태를 입력해주세요 : ').split()))
    map_status.append(status)

move_turn = 0
cnt = 1
while True:
    direction = (direction - 1) % 4
    move_row = row + direct_info[direction][0]
    move_col = col + direct_info[direction][1]
    if move_row < 0 or move_row > n or move_col < 0 or move_col > m:
        continue
    if map_check[move_row][move_col] == 0 and map_status[move_row][move_col] == 0:
        map_check[row][col] = 1
        row = move_row
        col = move_col
        cnt += 1
        move_turn = 0
        continue

    else:
        move_turn += 1

    if move_turn == 4:
        direction = (direction - 1) % 4
        move_row = row - direct_info[direction][0]
        move_col = col - direct_info[direction][1]
        if map_status[move_row][move_col] == 1 or move_row < 0 or move_row > n or move_col < 0 or move_col > m:
            break
        row = move_row
        col = move_col

print(cnt)