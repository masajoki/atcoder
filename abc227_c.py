N=int(input())
Nsqrt=int(N**0.5)
ans=0
for i in range(1,Nsqrt+1):
    for j in range(i,Nsqrt+1):
        k=int(N/i/j)
        if k>=j:
            ans+=k-j+1
        else:
            break
print(ans)