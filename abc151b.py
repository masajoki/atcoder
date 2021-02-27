N,K,M=map(int,input().split())
A=list(map(int,input().split()))

subtotal=0
for a in A:
    subtotal+=a

last=M*N-subtotal
if last>K:
    print(-1)
elif last <=0:
    print(0)
else:
    print(last)
