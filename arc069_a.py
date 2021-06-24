N,M=map(int,input().split())

temp=M//2
if N>=temp:
    print(temp)
elif N<temp:
    hoge=M-N*2
    print(N+hoge//4)
