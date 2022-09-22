import random
import copy

player_a = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
player_b = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


# 检查游戏是否结束
def check(player):
    count = 0
    for i in player:
        for j in i:
            if j == 0:
                count += 1
    if count == 0:
        return True
    else:
        return False


# 判定能否消除对手数字
def judge(col, num, arch):
    for i in range(3):
        if arch[i][col] == num:
            arch[i][col] = 0
    return arch


# 打印对局情况
def print_board():
    print('A:')
    for l in player_a:
        print(l)
    print('------------')
    print('B:')
    for l in player_b:
        print(l)
    print('A\'s point:' + str(count(player_a)))
    print('B\'s point:' + str(count(player_b)))


# 统计玩家分数 传入玩家列表 返回分数
def count(player):
    sum = 0
    count_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for i in range(3):
        count_dict[int(player[int(i)][0])] += 1
    for key in count_dict.keys():
        sum += int(key) * count_dict[key] * count_dict[key]
    count_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for i in range(3):
        count_dict[int(player[int(i)][1])] += 1
    for key in count_dict.keys():
        sum += int(key) * count_dict[key] * count_dict[key]
    count_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for i in range(3):
        count_dict[int(player[int(i)][2])] += 1
    for key in count_dict.keys():
        sum += int(key) * count_dict[key] * count_dict[key]
    return sum


def play(player, name, arch):
    print('Now is ' + name + '\'s round')
    # input('Type enter to get a random number:')
    print_board()
    get_num = random.randint(1, 6)
    print('Your result is:' + str(get_num))
    while 1:
        pos = input('type the position you want:')
        pos = pos.split()
        if player[int(pos[0])][int(pos[1])] == 0:
            player[int(pos[0])][int(pos[1])] = get_num
            break
        else:
            print('There is already a number on that position!')
    judge(int(pos[1]), get_num, arch)
    return player


def computer(player, arch):
    print('Now is Computer\'s round')
    get_num = random.randint(1, 6)
    print('Computer result is:' + str(get_num))
    max_point = -162  # 最高分差
    best_row = 0
    best_col = 0
    for row in range(3):
        for col in range(3):
            if player[row][col] != 0:
                continue
            else:
                copy_player = copy.deepcopy(player)  # 复制一份原表格
                copy_arch = copy.deepcopy(arch)
                copy_player[row][col] = get_num
                copy_arch = judge(col, get_num, copy_arch)
                point = count(copy_player) - count(copy_arch)
                if point > max_point:
                    best_row = row
                    best_col = col
                    print(str(row) + ' ' + str(col) + ' ' + str(point))
                    max_point = point
    player[best_row][best_col] = get_num
    judge(best_col, get_num, arch)

    return player


model_flag = 0
model = input('Which model, pvp or pve? (p/e)\n')
if model == 'p':
    model_flag = 1
while 1:
    # 玩家A进行操作
    player_a = play(player_a, 'A', player_b)
    print_board()
    if check(player_a):
        break
    # 根据model_flag决定是玩家B还是机器人进行操作
    if model_flag == 1:
        player_b = play(player_b, 'B', player_a)
    else:
        player_b = computer(player_b, player_a)
    print_board()
    if check(player_b):
        break
# 进行结算
if count(player_a) > count(player_b):
    print('A win!!')
elif count(player_a) < count(player_b):
    print('B win!!')
else:
    print('Draw!!')
print('Game Over !!')
