#B - Judge Status Summary
N=int(input())
S={}
S['AC']=0
S['WA']=0
S['TLE']=0
S['RE']=0

for i in range(N):
    s=input()
    if s in S:
        S[s]+=1
    else:
        S[s]=1
 
print("AC x "+str(S['AC']))
print("WA x "+str(S['WA']))
print("TLE x "+str(S['TLE']))
print("RE x "+str(S['RE']))

