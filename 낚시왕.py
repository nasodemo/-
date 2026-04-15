# temp에 이동 저장하고
# fight를 일괄로 처리하고
# 나머지를 sea에 반영해야 됨 !

r, c, m = map(int, input().split())
sea = []
for i in range(r):
    sea.append([0]*c)
for i in range(m):
    l = list(map(int, input().split()))
    l[0] -= 1
    l[1] -= 1
    sea[l[0]][l[1]] = l[2:]
def grap(col):
    for i in range(r):
        if sea[i][col] != 0:
            ans = sea[i][col][-1]
            sea[i][col] = 0
            return ans
    return 0

# s는 속력, d는 이동 방향, z는 크기이다. 
# d가 1인 경우는 위, 2인 경우는 아래, 3인 경우는 오른쪽, 4인 경우는 왼쪽을 의미한다
def move(i, j, l):
    s = l[0]
    d = l[1]
    if d < 3:
        s = s%((r-1)*2)
    else:
        s = s%((c-1)*2)
        
    flag = 1
    while(flag):
        if d == 1:
            i = i-s
            if i < 0:
                d = 2
                i *= -1
            if i >= r or i < 0:
                i -= 2*(i-(r-1))
                d = 1
            flag = 0
        elif d == 2:
            i = i+s
            if i >= r:
                d = 1
                i -= 2*(i-(r-1))
            if i >= r or i < 0:
                i *= -1
                d = 2
            flag = 0
        elif d == 3:
            
            j = j+s
            if j >= c:
                d = 4
                j -= 2*(j-(c-1))
            if j >= c or j < 0:
                j *= -1
                d = 3
            flag = 0

            
        elif d == 4:
            # print("변화 전:", i, j, s, d, l[-1])
            j = j-s
            if j < 0:
                d = 3
                j *= -1
            if j >= c or j < 0:
                j -= 2*(j-(c-1))
                d = 4
            flag = 0
            # print("변화 후:", i, j, s, d, l[-1])
            # print()    
    l[1] = d
    if temp_sea[i][j] == 0 or fight(i, j, l):
        temp_sea[i][j] = l
    return

def fight(i, j, l):
    if temp_sea[i][j][-1] < l[-1]:
        return 1
    else:
        return 0
# print(0, "start sea! :")
# for i in sea:
#     print(i)
ans = 0
for col in range(c):
    ans += grap(col)
    
    temp_sea = []
    for i in range(r):
        temp_sea.append([0]*c)
        
    for i in range(r):
        for j in range(c):
            if sea[i][j] != 0:
                temp = sea[i][j]
                move(i, j, temp)
    sea = temp_sea
    # print(col+1, "th sea :")
    # for i in sea:
    #     print(i)
    
print(ans)
    
