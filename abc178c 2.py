N=int(input())
# temp=N*(N-1) %(10**9+7)
# temp2=10**(N-2) %(10**9+7)
# ans=temp*temp2 %(10**9+7)
# print(ans)
# ↑このやりかただと同じ組み合わせができてしまうのでNG

m=10**9+7
ans=(10**N-2*9**N+8**N)%m
print(ans)