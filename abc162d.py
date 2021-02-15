
N=int(input())
S=list(input())
r=0
g=0
b=0
for s in S:
    if s=='R':
        r+=1
    elif s=='G':
        g+=1
    elif s=='B':
        b+=1
ans=r*b*g
for i in range(1,N//2+1):
    for j in range(N):
        if j+i*2 > N-1 :
            break
        else:
            s1=S[j]
            s2=S[j+i]
            s3=S[j+i*2]
            if s1!=s2 and s2!=s3 and s3!=s1:
                ans-=1
print(ans)