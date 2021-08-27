def main():
    N=int(input())
    # S=[]
    # T=[]
    dp=[[] for _ in range(N+1)]  #Trueのときの組み合わせ、Falseのときの組み合わせ
    dp[0]=[1,1]
    # for i in range(N):
    #     S.append(input())

    for i in range(N):
        tf=dp[i]
        s=input()
        if s=='AND': #ANDのときは、TRUEにするには直前がTRUEの組み合わせが変わらず、
            #FALSEにするには、直前がFALSEならi回は何でもよく（T/Fで2倍）
            # 直前がTRUEなら今回はFALSE（ので組み合わせ数はそのまま）
            dp[i+1]=(tf[0],tf[0]+tf[1]*2)
        else: #ORのときは、TRUEにするには直前がTRUEなら今回はTFどちらでもよく2倍、直前がFALSEならTRUEの場合のみ
            #FALSEにするには直前がFALSEで今回もFALSEでなければいけない。
            dp[i+1]=(tf[0]*2+tf[1],tf[1])

    print(dp[N][0])

if __name__ == "__main__":
    main()
#嬉しい初めてDPを自力で解けた

