n = int(input())
ans = []
way = [[-1, 0], [1, 0], [0, 1], [0, -1]]
for _ in range(n):
    h, w = map(int, input().split())
    base = []
    for i in range(h):
      l = list(input())
      base.append(l)
    key = list(input())
    if key[0] == "0":
        key = []
    go = []
    door = []
    
    def spread(temp):
      for k in way:
        step = temp[:]
        step[0] += k[0]
        step[1] += k[1]
        check(step[0], step[1])
      return
    
    def open(temp):
        i, j = temp[0], temp[1]
        if base[i][j].lower() in key:
            base[i][j] = "0"
            go.append([i, j])
            return 1
        return 0
    
    def check(i, j):
      global doc
      if i < 0 or i >= h or j < 0 or j >= w or base[i][j] == "*" or base[i][j] == "0":
        return 0
      if base[i][j] == "." or base[i][j] == "$" or base[i][j].lower() == base[i][j]:
        if base[i][j] == "$":
            doc += 1
        if base[i][j].lower() == base[i][j]:
            key.append(base[i][j])
        base[i][j] = "0"
        go.append([i, j])
      elif base[i][j].upper() == base[i][j]:
          door.append([i, j])
      return 1
    doc = 0
    for i in range(h):
      for j in range(w):
          if i == 0 or i == h-1 or j == 0 or j == w-1:
            check(i, j)
    while(True):
      # spread로 go 부터 들어간다.
      for temp in go:
        spread(temp)
      # open으로 가지고 있는 키로 다 딴다.
      flag = 0
      for temp in door:
          flag += open(temp)
      if not flag:
        break
      #만약 open한 문이 없으면 break
      #문 열었으면 go에다가 문의 좌표 넣고 spread
    # for i in base:
    #     print(i)
    ans.append(doc)
for i in ans:
    print(i)
