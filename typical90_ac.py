#typical90_ac.py
#029 - Long Bricks（★5）
W,N=map(int,input().split())
H=[0 for _ in range(W+1)]
L=[]
R=[]

for _ in range(N):
    l,r=map(int,input().split())
    L.append(l)
    R.append(r)

ans=[]
for i in range(N):
    height=max(H[L[i]:R[i]+1])+1
    for j in range(L[i],R[i]+1):
        H[j]=height
    ans.append(height)

for a in ans:
    print(a)