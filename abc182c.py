N=list(input())

# thanks to https://murashun.jp/blog/20200113-20.html
def popcount(x):
    '''xの立っているビット数をカウントする関数
    (xは64bit整数)'''

    # 2bitごとの組に分け、立っているビット数を2bitで表現する
    x = x - ((x >> 1) & 0x5555555555555555)

    # 4bit整数に 上位2bit + 下位2bit を計算した値を入れる
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)

    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f # 8bitごと
    x = x + (x >> 8) # 16bitごと
    x = x + (x >> 16) # 32bitごと
    x = x + (x >> 32) # 64bitごと = 全部の合計
    return x & 0x0000007f

ans=[]
nlen=len(N)
for i in range(1,2**nlen):
    tempslist=[]
    for j in range(len(N)):
        if i & (1 << j):
            tempslist.append(N[j])
    tempstr=map(str,tempslist)
    temp=int("".join(tempstr))
    if temp %3 ==0:
        usednum=popcount(i)
        ans.append(usednum)
if len(ans)==0:
    print(-1)
else:
    result=nlen-max(ans)
    print(result)




