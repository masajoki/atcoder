import collections 
S=list(input())

ans0=0
ans1=0
for i in range(0,len(S),2):
    if S[i]!='0':
        ans0+=1

for i in range(1,len(S),2):
    if S[i]!='1':
        ans0+=1  

for i in range(0,len(S),2):
    if S[i]!='1':
        ans1+=1

for i in range(1,len(S),2):
    if S[i]!='0':
        ans1+=1  

print(min(ans1,ans0))



