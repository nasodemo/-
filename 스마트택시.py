#19238
# 19238
N, M, fuel = map(int,input().split())
field = []
# 1은 벽
for i in range(N):
    field.append(list(map(int,input().split())))
start_i, start_j = map(int,input().split())
start_i, start_j = start_i-1, start_j-1
def print_map(map):
    print('start_print_field')
    for i in map:
        for j in i:
            print(j, end=' ')
        print()
    print('end_print_field')

# 연료 충전 후 남은 연료의 양 구하기
ans = 0
flag = 0

# 현 택시 위치상 최단 거리인 승객 태우기
# 1. 행번호 2. 열번호
# 소모한 양 2배 충전
# 음수면 사람
goal = {}

for i in range(1, M+1):
    # si, sj, ei, ej / 목적지가 같을 수 있음
    l = list(map(int,input().split()))
    for j, vj in enumerate(l):
        l[j] = vj-1
    goal[-i] = l[2:]
    field[l[0]][l[1]] = -i

def check(i, j, gone):
    if i < 0 or j < 0 or i >= N or j >= N:
        return 0
    if field[i][j] == 1:
        return 0
    if gone[i][j] == 1:
        return 0
    return 1

def go(si, sj, target = 0):
    global fuel
    count = 0
    way = [[0,1], [0, -1], [1,0], [-1, 0]]
    gone = [[0]*N for _ in range(N)]
    que = [[si, sj]]
    temp = []
    re = []
    while(que):
        a, b = que.pop()
        # print("que", que, temp)
        if check(a, b, gone) != 0:
            if target == 0 and field[a][b] < 0:
                re.append([a, b, field[a][b]])
                # print("t0", re)
            if target != 0 and a == target[0] and b == target[1]:
                re.append([a, b, field[a][b]])
                # print("t=1", re)
                break
            gone[a][b] = 1
            for l in way:
                temp.append([a+l[0], b+l[1]])
            # print(a, b, temp, que)
        if not que:
            # print("que", que, temp)
            if re:
                # print("t=1", re)
                break
            count += 1
            que = temp
            temp = []
    # print_map(gone)
    # print(re, count)
    re.sort()
    if re and count > fuel:
        return 0
    if not re:
        return 1
    fuel -= count
    if target:
        fuel += 2*count
    else:
        field[re[0][0]][re[0][1]] = 0
    return re[0]
loop = 0
while(True):
    # 쭉 돌아서 없으면 0
    re = go(start_i, start_j)
    # print(re)
    # 길이 없거나 기름이 없으면
    if type(re) != list:
        if loop != M or re == 0:
            flag = 1
        break
    t = goal[re[2]]
    re = go(re[0], re[1], t)
    if type(re) != list:
        if loop != M or re == 0:
            flag = 1
        break
    # 길이 없거나 기름이 떨어졌는지 
    # print_map(field)
    start_i, start_j = t[0], t[1]
    loop += 1
    # print(fuel, loop)
# print(loop)
if flag:
    print(-1)
else:
    print(fuel)


'''
너비우선 탐색 <- n
찾으면 지우고
너비우선 탐색으로 도착지 찾고 <- n
지우고
반복


20*20 사이즈에서 400하는걸

400번 반복 최대

즉

800*400이면 풀이 가능

'''
