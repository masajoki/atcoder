#abc236_b.py
N=int(input())
A=list(map(int,input().split()))
Ans=[0 for _ in range(N+1)]
for a in A:
    Ans[a]+=1

for i in range(1,N+1):
    if Ans[i]==3:
        print(i)
        exit()
