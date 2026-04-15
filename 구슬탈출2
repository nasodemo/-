#13460
n, m = map(int, input().split())
base = []
for i in range(n):
    base.append(list(input()))
def roll(way, test_map):
    blue = []
    red = []
    for i, vi in enumerate(test_map):
        for j, vj in enumerate(vi):
            if vj == "R":
                red = [i, j]
                test_map[i][j] = "."
            elif vj == "B":
                blue = [i, j]
                test_map[i][j] = "."
    start_b = blue[:]
    start_r = red[:]
    red_in = 0
    blue_in = 0
    # i = 0
    while(True):
        # print(red, blue)
        if not blue_in and blue[0] >= 0 and blue[0] < n and blue[1] >= 0 and blue[1] < m:
            if test_map[blue[0]][blue[1]] == "#" or test_map[blue[0]][blue[1]] == "R":
                blue[0] -= way[0]
                blue[1] -= way[1]
                test_map[blue[0]][blue[1]] = "B"
                blue_in = 2
        # print(red)
        blue[0] += way[0]
        blue[1] += way[1]
        red[0] += way[0]
        red[1] += way[1]
        if not blue_in and blue[0] >= 0 and blue[0] < n and blue[1] >= 0 and blue[1] < m:
            if test_map[blue[0]][blue[1]] == "#" or test_map[blue[0]][blue[1]] == "R":
                blue[0] -= way[0]
                blue[1] -= way[1]
                test_map[blue[0]][blue[1]] = "B"
                blue_in = 2
            elif test_map[blue[0]][blue[1]] == "O":
                blue_in = 1
        if not red_in and red[0] >= 0 and red[0] < n and red[1] >= 0 and red[1] < m:
            if test_map[red[0]][red[1]] == "#" or  test_map[red[0]][red[1]] == "B":
                red[0] -= way[0]
                red[1] -= way[1]
                test_map[red[0]][red[1]] = "R"
                red_in = 2
            elif test_map[red[0]][red[1]] == "O":
                red_in = 1
        if red_in and blue_in:
            break
        # i += 1
    # print(red_in)
    # print()
    # print(red, blue)
    if blue_in == 1:
        return 0, [] # 파란 공 들어감!
    elif red_in == 1:
        return 2, [] # 빨간 공 들어감!
    elif start_r == red and start_b == blue:
        return 3, [] # 이번엔 못 움직임!
    else:
        return 1, test_map # 일단 문제 없음!
flag = 0
way = [[-1, 0], [1, 0], [0, 1], [0, -1]]
que = []
for i in way:
    test_map = []
    for j in range(n):
        test_map.append(base[j][:])
    que.append([i, test_map])

for count in range(10):
    wait = []
    for i in que:
        check, escape = roll(i[0], i[1])
        if check == 1:
            for i in way:
                test_map = []
                for j in range(n):
                    test_map.append(escape[j][:])
                wait.append([i, test_map])
        elif check == 2:
            flag = 1
            break
    if flag == 1:
        break
    else:
        que = wait

if flag == 1:
    print(count+1)
else:
    print(-1)
        # 구슬을 돌리고
        # 괜찮으면 que에 way 넣어서 그 판때기 가지고 돌린다.
