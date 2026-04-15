#2206
import sys

n, m = map(int, sys.stdin.readline().split())
root_map = []
ans = [[[-1, -1] for j in range(m)] for i in range(n)]
for i in range(n):
    row = sys.stdin.readline().strip()
    row = list(row)
    for p, j in enumerate(row):
        if j == '1':
            ans[i][p] = 'X'
    root_map.append(row)
start = [0, 0, 0, 0]
ans[start[0]][start[1]] = [0, 0]

def root_map_finder(x, y, step, att):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    elif root_map[x][y] == '1': # 벽을 뚫는 프로세스
        if att >= 1:
            return False
        else:
            return 2
    if att == 0:
        if ans[x][y][0] == -1:
            ans[x][y][0] = step+1
            return True
        else:
            ans[x][y][0] = min(ans[x][y][0], step+1)
            return False
    elif att == 1:
        if ans[x][y][1] == -1:
            ans[x][y][1] = step+1
            return True
        elif ans[x][y][1] != -1:
            ans[x][y][1] = min(ans[x][y][1], step+1)
            return False
        
def root_map_go(x, y, step, att):
    que = []
    way = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    for i in range(4):
        re = root_map_finder(x+way[i][0], y+way[i][1], step, att)
        if re:
            if re == 2:
                que.append([x+way[i][0], y+way[i][1], step+1, att+1])
            else:
                que.append([x+way[i][0], y+way[i][1], step+1, att])
    return que

s = 1
while 1:
    if s:
        que = [start]
        s = 0
    queque = []
    for point in que:
        queque += root_map_go(point[0], point[1], point[2], point[3])
    que = queque
    # print(que)
    if len(que)==0:
        break

# for i in ans:
    # print(i)
if ans[n-1][m-1] == [-1, -1]:
    print(-1)
else:
    if -1 in ans[n-1][m-1]:
        ans[n-1][m-1].remove(-1)
    print(min(ans[n-1][m-1])+1)
