#abc173d.py
#これって大きい順に並び替えて、最大の人と２ばン目の人の間に入ればいいだけなのではないのか？

N=int(input())
Alist=list(map(int,input().split()))
Alist.sort(reverse=True)
kokochiyosa=Alist[0]
for i in range(1,N-1):
    kokochiyosa+=Alist[(i+1)//2]

print(kokochiyosa)

