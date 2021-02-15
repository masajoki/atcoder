N=int(input())
anslist=[]
testemony=[[ int() for _ in range(N) ]for _ in range(N)]


# testemony [ｎの人が][ｍの人についていう]


for n in range(N):
    A=int(input())
    for i in range(A):
        x,y=map(int,input().split())
        testemony[n][x]=y

for j in range(2**N):## jは組み合わせ、ビットが立ってるのが正直者
    honstonlytemp=[ int() for _ in range(N) ]
    honest=0
    for k in range(N):  
        if ((j >> k) &1 ): ## kの人が正直者だとすれば、各人の意見が正直者の人数と一致するか、ゼロになるはず。
            honest+=1
            for m in range(N):
                honstonlytemp[]



