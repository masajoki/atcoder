def main():

    S=list(input())
    N=len(S)
    LR=[0 for _  in range(N)]
    # L=[0 for _  in range(N)]
    l=0
    r=0

    for i in range(N):
        right=N-1-i
        if S[i]=='L':
            l+=1
            LR[i]=l
        elif S[i]=='R':
            l=0
        if S[right]=='R':
            r+=1
            LR[right]=r
        elif S[right]=='L':
            r=0

    A=[0 for _ in range(N)]

    for i in range(N):
        if S[i]=='R':
            if LR[i]%2==0:
                A[i+LR[i]]+=1
            else:
                A[i+LR[i]-1]+=1
        if S[i]=='L':
            if LR[i]%2==0:
                A[i-LR[i]]+=1
            else:
                A[i-LR[i]+1]+=1

    print(" ".join(map(str,A)))


if __name__ == '__main__':
    main()
