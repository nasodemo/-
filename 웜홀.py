#1865
import sys
input = sys.stdin.readline
INF = int(1e9)
def bell(start):
  if check[start] == 1:
    return False
  distance[start] = 0
  check_total = 1
  check[start] = 1
  in_roof_check = [0] * (N+1)
  in_roof_check[start] = 1
  step=graph[start][:]
  i = 0
  while(i<check_total):
    for l in step:
      cur_node = l[0]
      next_node = l[1]
      cost = l[2]
      if distance[cur_node] != INF and distance[next_node] > distance[cur_node] + cost:
        distance[next_node] = distance[cur_node] + cost
        if in_roof_check[next_node] == 0:
          in_roof_check[next_node] = 1
          check_total += 1
        if check[next_node] == 0:
          check[next_node] = 1
          step += graph[next_node][:]
          # print(check_total, i, distance, step)
        if check_total - 1 == i:
          return True
    i += 1
  return False
for _ in range(int(input())):
  N, M, W = map(int,input().split())
  graph = {}
  ans = 0
  for i in range(N):
    graph[i+1] = []
  for i in range(M):
    S,E,T = map(int,input().split())
    graph[S].append([S,E,T])
    graph[E].append([E,S,T])
  for i in range(W):
    S,E,T=map(int,input().split())
    graph[S].append([S,E,-T])
    if S == E:
      ans += 1
  check = [0]*(N+1)
  distance = [INF] * (N+1)
  for i in range(N-1):
    ans += bell(i+1)
  if ans:
    print("YES")
  else:
    print("NO")
