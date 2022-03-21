import operator

location = (1, 1)
n = int(input('공간의 크기를 입력해주세요 : '))
moves = input('이동할 계획서를 입력해주세요 :').split()

move_dict = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}
for move in moves:
    move_loc = tuple(map(operator.add, location, move_dict[move]))
    if move_loc[0] >= 1 and move_loc[0] <= n and move_loc[1] >= 1 and move_loc[1] <= n:
        location = move_loc
    # print(location)

print(location[0], location[1])
