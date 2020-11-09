N,M,X=map(int,input().split())
C=[]
for _ in range(N):
    c=list(map(int,input().split()))
    C.append(c)

minCost= 9999999999 #コストの初期値を十分に大きく
skill=[]

def initSkillScore(): #スキルの初期化
    skill.clear()
    for _ in range(M):
        skill.append(0)

for i in range(2**N): #N冊の参考書の組み合わせを生成bit列で表現 
    initSkillScore()
    cost=0
    for j in range(N): #ビットが立ってる参考書のコストとスキルを足し合わせる
        bit=(i>>j & 1) #右端のビットを取り出す
        if bit == 1:
            cost+=C[j][0] 
            for k in range(M):
                skill[k]+=C[j][k+1]
    if min(skill)>=X:
        minCost=min(minCost,cost)

if minCost == 9999999999:
    print(-1)
else:
    print(minCost)


