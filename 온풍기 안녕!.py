from collections import defaultdict
R, C, K = map(int,input().split())
temper = [[0]*C for _ in range(R)]
heat = []
target = []
for i in range(R):
    l = list(map(int,input().split()))
    for j in range(C):
        if l[j] == 5:
            target.append([i, j])
        elif l[j] > 0:
            heat.append([i, j, l[j]-1])
# 0 1 2 3
# 동 서 남 북
W = int(input())
wall = defaultdict(list)
for i in range(W):
    a, b, c = map(int,input().split())
    a -= 1
    b -= 1
    if c == 0: # 남북
        wall[(a, b)].append((a-1, b))
        wall[(a-1, b)].append((a, b))
    if c == 1: #동서
        wall[(a, b)].append((a,b+1))
        wall[(a,b+1)].append((a,b))

def check(i, j):
    if i < 0 or j < 0 or i >= R or j >= C:
        return 0    
    #TODO 벽 구현
    return 1
# step 1: 바람이 분다
way = [[0, 1], [0, -1], [-1, 0], [1, 0]]
def wind(l):
    sa, sb, sc = l[0], l[1], l[2]
    que = {(sa+way[sc][0], sb+way[sc][1])}
    t = 5
    temp = set()
    while(que and t > 0):
        ll = que.pop()
        a, b = ll[0], ll[1]
        temper[a][b] += t
        na, nb = a + way[sc][0], b + way[sc][1]
        if check(na, nb) and (na, nb) not in wall[(a,b)]:
            temp.add((na, nb))
        na, nb = a + way[sc][1], b + way[sc][0]
        if check(na, nb) and (na, nb) not in wall[(a,b)]:
            nna, nnb = na + way[sc][0], nb + way[sc][1]
            if check(nna, nnb) and (nna, nnb) not in wall[(na,nb)]:
                temp.add((nna, nnb))
        na, nb = a - way[sc][1], b - way[sc][0]
        if check(na, nb) and (na, nb) not in wall[(a,b)]:
            nna, nnb = na + way[sc][0], nb + way[sc][1]
            if check(nna, nnb) and (nna, nnb) not in wall[(na,nb)]:
                temp.add((nna, nnb))
        if not que:
            # for i in temp:
            #     print(i, end=' ')
            # print("t", t)
            t = t - 1
            que = temp
            temp = set()
    return
# step 2: 
def mod():
    global temper
    ndata = [[0]*C for _ in range(R)]
    # 남북 비교
    for j in range(C):
        for i in range(R-1):
            if (i+1, j) in wall[(i, j)]:
                continue
            if temper[i][j] > temper[i+1][j]:
                b, bb = i, j
                g, gg = i+1, j
            elif temper[i][j] < temper[i+1][j]:
                b, bb = i+1, j
                g, gg = i, j
            else:
                continue
            amount = int(abs(temper[i][j] - temper[i+1][j])//4)
            ndata[b][bb] -= amount
            ndata[g][gg] += amount
    # 동서 비교
    for i in range(R):
        for j in range(C-1):
            if (i, j+1) in wall[(i, j)]:
                continue
            if temper[i][j] > temper[i][j+1]:
                b, bb = i, j
                g, gg = i, j+1
            elif temper[i][j] < temper[i][j+1]:
                b, bb = i, j+1
                g, gg = i, j
            else:
                continue
            amount = int(abs(temper[i][j] - temper[i][j+1])//4)
            ndata[b][bb] -= amount
            ndata[g][gg] += amount
    for i in range(R):
        for j in range(C):
            temper[i][j] += ndata[i][j]
    return
def dec():
    global temper
    for i in range(R):
        for j in range(C):
            if temper[i][j] != 0 and (i == 0 or j == 0 or i == R-1 or j == C-1):
                temper[i][j] -= 1
    return
def count_end():
    count = 0
    for l in target:
        if temper[l[0]][l[1]] >= K:
            count += 1
    if count == len(target):
        return 1
    return 0
count = 0
def print_(l):
    for i in range(len(l)):
        print(l[i])
    print("end")
    return
ans = 0
while(True):
    for l in heat:
        wind(l)
#print_(temper)
    mod()
#print_(temper)
    dec()
    ans += 1
    if count_end(): break
    if ans == 101:
        break
print(ans)
