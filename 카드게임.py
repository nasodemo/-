import sys
n, m, k = map(int, input().split())
card = [0]*n
l = list(map(int, sys.stdin.readline().split()))
ch = list(map(int, sys.stdin.readline().split()))
temp =  0
for i in l:
    card[i-1] = -1
    if i > temp:
        temp = i-1
for i in range(len(card)-1, -1, -1):
    if card[i] == 0:
        card[i] = temp
    else:
        temp = i
ans = [] 
for i in ch:
    target = i # 이미 -1 해서 저장했으니 i는 사실상 +1임 ㅇㅇ
    while(True):
        vj = card[target]
        if vj == -1:
            break
        else:
            target = vj
    card[target] = target + 1
    ans.append(target+1)
    
for i in ans:
    print(i)
    # 해당 위치의 카드 한 칸 위를 본다
    # -1이면 카드를 내고 +1의 i 값을 넣어둔다.
    
    # -1이 아니면 해당 위치의 값을 본다.
    # -1이면 반복
    # -1이 아니면 해당 위치의 값이 가르키는 값을 본다.
