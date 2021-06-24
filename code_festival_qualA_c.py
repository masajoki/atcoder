A,B=map(int,input().split())
ans=0

ans+=B//4
ans-=B//100
ans+=B//400

ans-=(A-1)//4
ans+=(A-1)//100
ans-=(A-1)//400
print(ans)