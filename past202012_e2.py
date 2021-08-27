H,W=map(int,input().split())
S=[]
T=[]
for i in range(H):
    S.append(input())
for i in range(H):
    T.append(input())






ans=False

def check(T):
    hankoH=len(T)
    hankoW=len(T[0])
    #はんこの位置
    chk=max(W,H) #はんこを傾けたときにずらす位置の最大
    for h in range(-chk,chk):
        for w in range(-chk,chk):
            possible=True
                    
            #はんこの一致確認
            for i in range(hankoH):
                for j in range(hankoW):
                    si=i+h
                    sj=j+w
                    if T[i][j]=='#':    
                        if 0<=si<H and 0<=sj<W:
                            if S[si][sj]!='.':
                                possible=False
                        else:
                            possible=False
        
            if possible ==True:
                # print(h,w)
                print("Yes")
                exit()


check(T)
for i in range(3):
    T=list(map(list,zip(*T)))
    T.reverse()

    # for t in T:
    #     print(t)

    check(T)

print("No")
