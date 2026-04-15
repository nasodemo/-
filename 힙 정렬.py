N = int(input())
dp=[0, 1]
def go_up(index):
    while((index//2) > 0 and dp[index] > dp[index//2]):
        dp[index], dp[index//2] = dp[index//2], dp[index]
        index = index//2
    return
for i in range(2, N+1):
    dp.append(i)
    dp[-1], dp[-2] = dp[-2], dp[-1]
    go_up(i-1)
for i in range(N):
    print(dp[i+1], end=' ')
