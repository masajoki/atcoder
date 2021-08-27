N=int(input())
A=list(map(int,input().split()))
Nums=[0 for _ in range(10**5+1)]
for a in A:
    Nums[a]+=1

nonzero=list(filter(lambda x:x>0, Nums ))
evens=list(filter(lambda x:x%2==0,nonzero))
print(len(nonzero)-len(evens)%2)