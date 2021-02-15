a,b,k=map(int,input().split())
temp=a-k 
ans1=max(0,temp)
temp2=max(0,b+min(temp,0))
print(ans1,temp2)