N=int(input())
ans=N
ans-=N//3            
ans-=N//5
ans+=N//15
print(ans)