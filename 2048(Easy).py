n = int(input())
base = []
for i in range(n):
    base.append(list(map(int, input().split())))

## 4**5 이동해서 걍 큰거 구해보면 될 듯?

def shrink(l):
    ans = []
    target_v = 0
    target_p = 100
    flag = 0
    for i, vi in enumerate(l):
        if flag == 0:
            target_p = min(target_p, i)
            if vi != 0:
                target_v = vi
                l[target_p] = target_v
                l[i] = 0
                flag = 1
        elif flag == 1 and vi != 0:
            l[i] = 0
            if vi == target_v:
                l[target_p] = target_v*2
                target_p += 1
                target_v = 0
                flag = 0
            else:
                l[target_p] = target_v
                target_v = vi
                l[target_p+1] = target_v
                target_p += 1
                flag = 1
        else:
            continue
    return

def right(use):
    for r in use:  
        r.reverse()
        shrink(r)
        r.reverse()
    return
def left(use):
    for r in use:
        r = shrink(r)
    return
def up(use):
    for c in range(n):
        col = []
        for r in range(n):
            col.append(use[r][c])
        shrink(col)
        for r in range(n):
            use[r][c] = col[r]
    return
def down(use):
    for c in range(n):
        col = []
        for r in range(n-1, -1, -1):
            col.append(use[r][c])
        shrink(col)
        for r in range(n-1, -1, -1):
            use[r][c] = col[r]
    return

way = [right, left, up, down]
# way = [up]
def handle(l, depth):
    ans = 0
    if depth == 6:
        for i in l: 
            ans = max(ans, max(i))
            # print(i)
        return ans
    ## 모든 경우의 수를 찾자
    for func in way:
        use = []
        for i in l:
            use.append(i[:])
        func(use)
        ans = max(ans, handle(use, depth + 1))
    return ans

if n == 1:
    print(base[0][0])
else:
    print(handle(base, 1))

"""
5
0 0 0 0 2
0 4 0 0 4
2 2 0 0 0
2 4 0 0 100
8 0 4 4 0

3
1024 1024 0
0 0 1024
0 0 1024
"""
