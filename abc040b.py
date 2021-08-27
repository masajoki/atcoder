ans=9999999999
N=int(input())
Ns=int(N**0.5)

for i in range(1,Ns+1):
    temp=N-i*(N//i)+(N//i-i)
    ans=min(temp,ans)
print(ans)