# <>>>><<<><><>
S=list(input())
S.append("") #終端
# <<<<<>>
# 0<1<2<3<4<5>1>0
# 0< 2>1>0< 1<2<3<4 >0< 4>3>2>1 >0< 1 >0
# >>><<><<<<><><>>><>>><<<<
  -4 +2 -1 +4 -1 +1 -1 +1 -10 +2
  3 0 2  0  4  0  1 0  10  0  2  
      
dec=[]
asc=[]

last=S[0]

repeat=1
for i in range(1,len(S)):
    if S[i] == '<':
        if last=='<':
            repeat+=1
        else:
            dec.append(repeat)
            repeat=1
        last=S[i]

    elif S[i]=='>' :
        if last=='>':
            repeat+=1
        else:
            asc.append(repeat)        
            repeat=1
        last=S[i]
    else:
        if last=='>' :
            dec.append(repeat)        
        else:
            asc.append(repeat)

print(asc)
print(dec)

for i in des:
    i

