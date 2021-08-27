#058 - Original Calculator（★4）
N,K=map(int,input().split())
mod=100000

ans=N
temp=N
hoge=0
dic={}
for i in range(K):
    temp=temp+sum(list(map(int,list(str(temp)))))
    temp%=mod
    if temp==0:
        print(temp)
        exit()
    if temp in dic.keys():
        hoge=i-dic[temp]
        break
    else:
        dic[temp]=i

if hoge>0:
    rest=(K-i)%hoge
    if rest-1>=0:
        for i in range(rest-1):
            temp=temp+sum(list(map(int,list(str(temp)))))%mod
            temp%=mod

print(temp)

