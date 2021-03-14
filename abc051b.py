#B - Sum of Three Integers 
K,S=map(int,input().split())
# 0<=X,Y,Z<=KかつX+Y+Z=Sを満たすX,Y,Zは何通りあるか

ans=0
imin=max(0,S-2*K)
#Sこ並んだ石の隙間に2本の棒を配置する組み合わせ、を考える
# 1つの隙間はK個の石しか含めないのでそれを制約にしてループ回すだけ。
for i in range(imin,K+1):
    jmin=max(S-K,i)
    jmax=min(i+K+1,S+1)
    for j in range(jmin,jmax):
        ans+=1
print(ans)


     