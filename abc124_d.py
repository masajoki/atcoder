#尺取。めんどくさがらずに紙に書くとわかる。

N,K=map(int,input().split())
S=input()
onecnt=0
zerocnt=0
one=[]
zero=[]
current=S[0]
count=1
for n in range(1,N):
    if S[n]==current:
        count+=1
    else:
        if current=='1':
            one.append(count)
        else:
            zero.append(count)
        current=S[n]
        count=1
if current=='1':
    one.append(count)
else:
    zero.append(count)

onecnt=len(one)
zerocnt=len(zero)

if zerocnt<=K:
    print(N)
    exit()


temp=0
for i in range(K):
    temp+=one[i]
    temp+=zero[i]

if S[0]=='1' and K<onecnt:
    temp+=one[K]


ans=temp
for i in range(zerocnt): #この辺がややこしい
    if i+K < zerocnt:
        temp-=zero[i]
        temp+=zero[i+K]

    if S[0]=='1':
        temp-=one[i]
        if i+K+1 < onecnt:
            temp+=one[i+K+1]
    else:
        if i-1>=0:
            temp-=one[i-1]
        if i+K<onecnt:
            temp+=one[i+K]

    ans=max(temp,ans)

print(ans)
