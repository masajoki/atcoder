def main():
    from collections import Counter
    N=int(input())
    A=list(map(int,input().split()))
    Asum={}
    Asum[0]=1
    t=0
    for a in A:
        t+=a
        if t in Asum:
            Asum[t]+=1
        else:
            Asum[t]=1
    c=Counter(Asum)
    ans=0
    for v in c.values():
        if v>1:
            ans+=((v-1)**2+v-1)//2 #合計が同じ値の時について、1つを選ぶ場合と2つを選ぶ場合の合計が組み合わせの数
    print(ans)
main()