# N:正の整数
# ある素数p
# 正の整数e
# z=p**eと表せる
# N % z == 0
# N = N/Z

# 因数分解
# 各因数は1からカウントアップして取れるだけ取る

#難しかったポイント
# 要するに因数分解だと気づく
# 因数ごとの組み合わせ（1からカウントアップして生けるところまで行けばよかった）
# 割っていって素数が残ったときの取り扱いを個別に考えないといけない
# 素数関連嫌い

import math
N=int(input())
p={}

if N<=1:
    print (0)
    exit()


for i in range(2,int(math.sqrt(N)+1)):
    while N % i == 0:
        if i in p:
            p[i]+=1
        else:
            p[i]=1
        N/=i

#素数が残った場合
if N!=1:
    p[N]=1

ans=0
for Pi in p.values():
    for j in range (1,Pi+1) :
        if Pi >= j:
            Pi  -= j
            ans +=1

if ans==0:
    print(1)
    exit()
print (ans)