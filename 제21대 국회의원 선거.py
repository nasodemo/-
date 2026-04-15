import copy
pn, tp = map(int, input().split())
raw_pd = []
non = 300 - 47
tm = 0
for i in range(pn):
    p = input().split()
    p[1] = int(p[1])
    non -= p[1] # 무소속 의석수 non
    p[2] = int(p[2])
    tm += p[2]
    raw_pd.append(p)

pd = []
non_pd = []
pm = 0
for i, p in enumerate(raw_pd):
    p.append(p[2]/tm) # 순수 득표율 
    raw_pd[i] = p
    if p[1] < 5 and p[3] < 0.03:
        non += p[1] # 무소속 의석수 + 의석할당정당이 아닌 정당의 지역구 당선인 수 총합
        non_pd.append(p)
    else:
        pm += p[2] # 의석할당정당의 총 투표자 수 pm
        pd.append(p)
for i, p in enumerate(pd):
    p.append(p[2]/pm) # 비례대표국회의원선거 득표비율 pi를 p[4]에 저장 
                                #(p_i)는 전체 유효표에 대한 득표비율이 아니고, 의석할당정당의 득표수를 모든 의석할당정당의 득표수의 합계로 나누어 다시 산출됨에 주의한다.

s = []
s_sum = 0 # si들 sum
for i, p in enumerate(pd):
    ss = ((300-(non))*p[4] - p[1])/2
    if ss >= 1:
        ss = round(ss)
    else:
        ss = 0
    s_sum += ss
    s.append(p + [ss]) # si[5]에 si(연동 배분 의석 수) 저장

s_dum = copy.deepcopy(s)
sm_dum = 0
if s_sum < 30:
    for i, p in enumerate(pd):
        si = s[i]
        k = si[5] + (30-s_sum)*p[4]
        int_k = int(k)
        s[i][5] = int_k
        sm_dum += int_k # 산정 의석 정수 부분 합계
        s_dum[i][5] = k - int_k # 산정 의석 소수 부분 저장
elif s_sum > 30:
    for i, p in enumerate(pd):
        si = s[i]
        k = (30*si[5])/s_sum
        int_k = int(k)
        s[i][5] = int_k
        sm_dum += int_k
        s_dum[i][5] = k - int_k
s_dum.sort(key=lambda x:x[5], reverse=True)
while sm_dum != 30:
    for i, p in enumerate(s_dum):
        for j, jp in enumerate(s): # 소수점 이하의 수가 완전히 같으면 기호가 더 작은, 먼저 입력된 정당에 의석을 우선 배분한다.
            # print(p, jp)
            if p[0] == jp[0]:
                s[j][5] += 1
                sm_dum += 1
                if sm_dum == 30:
                    break
        if sm_dum == 30:
            break
t = []
t_dum = []
tm_dum = 0
for i, p in enumerate(pd):
    k = 17*p[4]
    int_k = int(k)
    tm_dum += int_k
    t.append(p+[int_k])
    t_dum.append(p+[k - int_k])
t_dum.sort(key=lambda x:x[5], reverse=True)
# print(t)
# print()
# print(t_dum)
while tm_dum != 17:
    for i, p in enumerate(t_dum):
        for j, jp in enumerate(t):
            if p[0] == jp[0]:
                t[j][5] += 1
                tm_dum += 1
                if tm_dum == 17:
                    break
        if tm_dum == 17:
            break
# print()
# print(t)
output = []
for i in range(len(pd)):
    output.append([pd[i][0], -(pd[i][1] + s[i][5] + t[i][5])])
for i in range(len(non_pd)):
    output.append([non_pd[i][0], -non_pd[i][1]])
output.sort(key=lambda x:(x[1], x[0]))
for i in output:
    print(i[0], -i[1])
