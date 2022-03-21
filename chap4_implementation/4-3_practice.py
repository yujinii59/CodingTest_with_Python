import string
import operator

location = input('현재 위치를 입력해주세요.: ')
cols = list(string.ascii_lowercase[:8])
row = int(location[1])
col = cols.index(location[0])

moves = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
cnt = 0
for move in moves:
    move_row = row + move[1]
    move_col = col + move[0]
    if move_row >= 1 and move_row <= 8 and move_col >= 1 and move_col <= 8:
        cnt += 1
print(cnt)