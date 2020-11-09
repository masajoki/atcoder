#1000が8の倍数なので、下3桁が8の倍数なら8の倍数
T=input()
S=list(T)
S.sort()
SS=''.join(S)

eight2dig=[]
for i in range(2,13):
    temp=i*8
    s=str(temp)
    sl=list(s)
    sl.sort()
    eight2dig.append(''.join(sl))

eight3dig=[]
for i in range(13,125):
    temp=i*8
    s=str(temp)
    sl=list(s)
    sl.sort()
    eight3dig.append(''.join(sl))

if len(T) == 1 and int(T)==8:
    print('Yes')
elif len(T) == 2:
    for p in eight2dig:
        if p in SS:
            print('Yes')
            exit()
    print('No')
elif len(T) > 2:
    if '888' in SS:
        print('Yes')
        exit()
    for p in eight3dig:
        found=True
        lasts=''
        for a in p:
            if lasts==a:
                lasts=a
                temp=a+lasts

                if temp not in SS:
                    found=False
                    continue
            elif a not in SS:
                lasts=a
                found=False
            else:
                lasts=a
                found=False
        if found:
            print('Yes')
            exit()
    print('No')
