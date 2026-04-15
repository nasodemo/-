#10775
import sys

g = int(input())
p = int(input())
l = [0]*g
sequence = [0]*g
flag = 0
for i in range(p):
    if flag:
        k = int(sys.stdin.readline())
        # print(l)
    else:
        k = int(sys.stdin.readline()) - 1
        if k >= g:
            k = g-1
        # 본 게임
        while(True):
            point = k + sequence[k]
            sequence[k] -= 1
            if point < 0:
                flag = 1
                break
            if l[point] == 0:
                l[point] = 1
                break
            else:
                continue
# print(sequence)
print(sum(l))
'''
4
3
4
1
1
'''
    
