def go(t):
  m_t = 32001
  for i in node[t]:
    check[i] -= 1
    if check[i] == 0:
      m_t = min(i, m_t)
  return m_t
def find_min_pr(t):
  min_pr = 32001
  for i in range(t, N+1):
    if check[i] == 0:
      min_pr = i
      return min_pr
  return min_pr
N, M = map(int,input().split())
node = {}
min_pr = 1
check = [0]*(N+1)
for i in range(N):
  node[i+1] = []
for _ in range(M):
  A, B = map(int,input().split())
  if A == B:
    continue
  node[A].append(B)
  check[B] += 1
  if min_pr == B:
    min_pr = find_min_pr(min_pr)
que =[min_pr]
check[min_pr] = -1
save = find_min_pr(min_pr)
flag = 1
while(que):
  t = que.pop()
  print(t, end=' ')
  check[t] = -1
  m_t = go(t)
  save = find_min_pr(min(m_t, save))
  que.append(save)
  # print(que, m_t, save, check)
  if save == 32001:
    break
'''
1. 종속 없는 놈 중 가장 빠른 놈 출력
 (입력 받으면서 저장)
2. 종속 받는 놈의 종속 제거
( 두 번째로 종속 없었던 놈 중 두 번째였던 놈 vs 새로 종속 없어진 놈 비교)
 (vs를 승리한 놈과 다음 절차 수행)
3. 종속 없는 놈 중 가장 빠른 놈 출력

결과: 이분 탐색 온 몸 비틀기?
'''
