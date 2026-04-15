'''
N

물고기 넣기

어항 쌓기

무한 공중 부양

N-1 - C = 높이
ep - rp = 너비
end_r - 1 + N-1 - C < N - end_r
ep부터 N까지의 길이는 높이 이상이어야만 함

조절

다시 무한 공중 부양

일렬로 쌓기
'''


N, K = map(int,input().split())
data = list(map(int,input().split()))
fly = [[0]*N for _ in range(N)]
for i in range(N):
    # for j in range(N):
    fly[-1][i] = data[i]
def put_fish(fly):
    low = min(fly[-1])
    for i in range(N):
        if fly[-1][i] == low:
            fly[-1][i] += 1
    return fly
def stack_boll(fly):
    fly[-2][1] = fly[-1][0]
    fly[-1][0] = 0
    return fly
def print_fly():
    for i in fly:
        for j in i:
            print(j, end=" ")
        print()
    print("End print Fly")
    return
def produce():
    c_point = 0
    end_c = 0
    for i in range(N):
        if c_point == 0 and fly[-2][i] != 0:
            c_point = i
        if c_point and fly[-2][i] == 0:
            end_c = i
            break
    r_point = -1
    for i in range(N-1, -1, -1):
        if fly[i][c_point] == 0:
            r_point = i
            break
    if end_c == 0:
        end_c = N
    return c_point, end_c, r_point
'''


'''

def step_rotate(fly):
    c_point, end_c, r_point = produce()
    # print(c_point, end_c, r_point)
    if N - r_point - 1 > N - end_c or end_c == N: # TODO 능지 이슈로 식이 정확한지 모르겠음
        return 0
    # N에서 부족한 만큼 위로 올라가 있음
    for i in range(c_point, end_c):
        b = i
        for j in range(N-1, r_point, -1):
            a = j
            fly[N-1 - (end_c - i)][end_c + (N-1 - j)] = fly[a][b]
            fly[a][b] = 0
    return 1
def moder(fly):
    temp = [[0]*N for _ in range(N)]
    for i in range(0, N-1):
        for j in range(N):
            a = abs(fly[i][j] - fly[i+1][j])//5
            if a == 0 or fly[i][j] == 0 or fly[i+1][j] == 0: continue
            if fly[i][j] > fly[i+1][j]:
                temp[i][j] -= a
                temp[i+1][j] += a
            else:
                temp[i][j] += a
                temp[i+1][j] -= a
    for j in range(0, N-1):
        for i in range(N):
            a = abs(fly[i][j] - fly[i][j+1])//5
            if a == 0 or fly[i][j] == 0 or fly[i][j+1] == 0: continue
            if fly[i][j] > fly[i][j+1]:
                temp[i][j] -= a
                temp[i][j+1] += a
            else:
                temp[i][j] += a
                temp[i][j+1] -= a
    for i in range(0, N):
        for j in range(N):
            fly[i][j] += temp[i][j]
    return
def linear(fly):
    c_point, end_c, r_point = produce()
    # print(c_point, end_c, r_point)
    a, b = N-1, 0
    for j in range(c_point, end_c):
        for i in range(N-1, r_point, -1):
            # print(a, b, i, j, fly[i][j])
            fly[a][b] = fly[i][j]
            fly[i][j] = 0
            b += 1
    return
def half_rotate(fly):
    a = N-2
    b = N//2
    i = N-1
    for j in range(N//2-1, -1, -1):
        fly[a][b] = fly[i][j]
        fly[i][j] = 0
        b += 1
    a = N-4
    b = N//2+N//4
    for i in range(N-1, N-3, -1):
        for j in range(N//2+N//4-1, N//2-1, -1):
            fly[a][b] = fly[i][j]
            fly[i][j] = 0
            b += 1
        a += 1
        b = N//2+N//4
    return
def check_end(fly):
    if K < max(fly[-1]) - min(fly[-1]):
        return 1
    return 0
ans = 0
while(True):
    put_fish(fly)
    stack_boll(fly)
    # print(step_rotate(fly))
    while(step_rotate(fly) == 1): continue
    # print_fly()
    moder(fly)
    linear(fly)
    half_rotate(fly)
    moder(fly)
    linear(fly)
    # break
    ans += 1
    if check_end(fly) == 0:
        break
print(ans)
