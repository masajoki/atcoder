import math
S,P=map(int,input().split())
Ptemp=P
while Ptemp>0:
    for j in range(P+1):
        if j<=Ptemp:
            if math.floor(S*(100+j)/100)==S:
                continue
            else:
                if Ptemp-j>=0:
                    S=math.floor(S*(100+j)/100)
                Ptemp-=j
                break

print(S)        
