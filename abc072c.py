N=int(input())
A=list(map(int,input().split()))
S=[0 for i in range(10**5+10)]

for a in A:
    S[a]+=1

maxsum=0
for i in range(10**5):
    maxsum=max(maxsum,S[i]+S[i+1]+S[i+2])

print(maxsum)