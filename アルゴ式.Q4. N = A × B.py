#アルゴ式.Q4. N = A × B.py
N=int(input())
ans=10**18
for i in range(1+int(N**0.5),0,-1):
    if N%i==0:
        t=N//i
        ans=min(i+t,ans)
print(ans)

