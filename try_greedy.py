import random

player_a = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
player_b = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
balance = 2.5  # 权重

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


def judge(col, num, arch):
    for i in range(3):
        if arch[i][col] == num:
            arch[i][col] = 0


def print_board():
    print('A:')
    for l in player_a:
        print(l)
    print('------------')
    print('B:')
    for l in player_b:
        print(l)


def count(player):
    sum = 0
    count_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, balance: 0}
    for i in range(3):
        count_dict[int(player[int(i)][0])] += 1
    for key in count_dict.keys():
        sum += int(key) * count_dict[key] * count_dict[key]
    count_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, balance: 0}
    for i in range(3):
        count_dict[int(player[int(i)][1])] += 1
    for key in count_dict.keys():
        sum += int(key) * count_dict[key] * count_dict[key]
    count_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, balance: 0}
    for i in range(3):
        count_dict[int(player[int(i)][2])] += 1
    for key in count_dict.keys():
        sum += int(key) * count_dict[key] * count_dict[key]
    return sum


def play(player, name, arch):
    print('Now is ' + name + '\'s round')
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


def greedy(number):
    player_b_copy_1 = player_b
    i_max = 0  # 记录最贪i
    j_max = 0  # 记录最贪j
    cnt_max = 0  # 记录最贪分
    # 最上方还有一个权重balance全局变量。

    for i in range(0, 3):
        for j in range(0, 3):
            if player_b_copy_1[i][j] == 0:
                player_b_copy_1[i][j] = balance

    player_b_copy_2 = player_b_copy_1

    for i in range(0, 3):
        for j in range(0, 3):
            if player_b_copy_2[i][j] == balance:
                player_b_copy_2[i][j] = number
                if count(player_b_copy_2) > cnt_max:
                    cnt_max = count(player_b_copy_2)
                    i_max = i
                    j_max = j
                player_b_copy_2 = player_b_copy_1
                player_b_copy_2[i][j] = balance

    # 全还原，还没
    for i in range(0, 3):
        for j in range(0, 3):
            if player_b_copy_1[i][j] == balance:
                player_b_copy_1[i][j] = 0
            if player_b_copy_2[i][j] == balance:
                player_b_copy_2[i][j] = 0
            if player_b[i][j] == balance:
                player_b[i][j] = 0

    a = [i_max, j_max]
    return a


def play_ai(player, name, arch):
    print('Now is ai ' + name + '\'s round')
    print_board()
    get_num = random.randint(1, 6)
    print('Your result is:' + str(get_num))
    # 与play函数只改了这里，调用greedy()，并直接按照返回值输出。
    try_1 = greedy(get_num)
    player[int(try_1[0])][int(try_1[1])] = get_num

    judge(int(try_1[1]), get_num, arch)
    return player


#####

while 1:
    player_a = play(player_a, 'A', player_b)
    print_board()
    print('A\'s point:' + str(count(player_a)))
    print('B\'s point:' + str(count(player_b)))
    if check(player_a):
        break
    player_b = play_ai(player_b, 'B', player_a)
    print('A\'s point:' + str(count(player_a)))
    print('B\'s point:' + str(count(player_b)))
    if check(player_b):
        break
if count(player_a) > count(player_b):
    print('A win!!')
elif count(player_a) < count(player_b):
    print('B win!!')
else:
    print('平局')
print('Game Over !!')
