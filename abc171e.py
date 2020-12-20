N=int(input())
A=list(map(int,input().split()))
allxored=A[0]
for i in range(1,N):
    allxored ^= A[i] # ^はXOR、XORは2回やるともとに戻る。RAIDもこれ。
for a in A:
    print(allxored^a,end=' ')
print()
