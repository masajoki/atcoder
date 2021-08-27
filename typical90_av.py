# Bi(部分点) > Ai -Bi(加点) なので
# Bi, Ai-Bi を 大きい順に並べれば、
# Ai-Bi が選ばれるのにBiが選ばれないということはない
# 貪欲法
N,K=map(int,input().split())
T=[]
for i in range(N):
    a,b=map(int,input().split())
    T.append(b)
    T.append(a-b)
T.sort(reverse=True)
print(sum(T[0:K]))