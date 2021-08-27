N,K=map(int,input().split())
C=list(map(int,input().split()))
nums={}

for i in range(K):
    if C[i] in nums.keys():
        nums[C[i]]+=1
    else:
        nums[C[i]]=1


temp=len(nums.keys())
ans=temp
for j in range(N-K):
    nums[C[j]]-=1
    if nums[C[j]]==0:
        temp-=1
    t=j+K
    if C[t] in nums.keys():
        if nums[C[t]]==0:
            temp+=1
        nums[C[t]]+=1
    else:
        temp+=1
        nums[C[t]] =1
    ans=max(temp,ans)
print(ans)
               
    
