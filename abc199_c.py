N=int(input())
S=list(input())
Q=int(input())
T=[]
A=[]
B=[]

for i in range(Q):
    t,a,b=map(int,input().split())
    T.append(t)
    A.append(a)
    B.append(b)

swapped=False
for i in range(Q):
    if T[i]==2:
        if swapped:
            swapped=False
        else:
            swapped=True
    else:
        if swapped:
            if 1<=A[i]<=N:
                a=A[i]+N
            else:
                a=A[i]-N
            if 1<=B[i]<=N:
                b=B[i]+N
            else:
                b=B[i]-N
        else:
            a=A[i]
            b=B[i]
        ta=S[a-1]
        tb=S[b-1]
        S[a-1]=tb            
        S[b-1]=ta            

if swapped:
    ans=S[N:]+S[0:N]
    print("".join(ans))
else:
    print("".join(S))