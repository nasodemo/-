ind = input()
sd = ("+", "-")
ld = ("*", "/")
def printLe(le):
    if len(le) < 1:
        return le
    for i in range(len(le)):
        print(le[i], end="")
    return []
def endPart(le, cal):
    if len(le) > 0:
        for i in le:
            print(i, end="")
    if len(cal) > 0:
        lencal = len(cal)
        for cc in range(lencal-1, -1, -1):
            print(cal.pop(), end="")
    return le, cal

def main(ind):
    le = []
    cal = []
    flag = 0
    for j, i in enumerate(ind):
        # print("\ni :", i, "and flag: ", flag)
        # print("main :", ind[j+1:])
        if i == ")":
            if flag == 0:
                endPart(le, cal)
                return [[], []]
            elif flag > 0:
                flag -= 1
        elif i == "(":
            if flag == 0:
                le = printLe(le)
                main(ind[j+1:])
            flag += 1
        elif flag != 0:
            pass
        elif i in sd:
            le = printLe(le)
            
            lencal = len(cal)
            for cc in range(lencal-1, -1, -1):
                print(cal[cc], end="")
            cal = []
            cal.append(i)
        elif i in ld:
            le = printLe(le)
            
            lencal = len(cal)
            for cc in range(lencal-1, -1, -1):
                if cal[cc] in ld:
                    print(cal.pop(), end="")
                else:
                    break
                
            cal.append(i)
        else:
            le.append(i)
    # print("check",le, cal)
    return [le, cal]

            
            
a = main(ind)
endPart(a[0], a[1])
