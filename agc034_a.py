N,A,B,C,D=map(int,input().split())
S=input()
acPath=S[A-1:C]
bdPath=S[B-1:D]

if D>C:
    if "##" not in S[A:C] and  "##" not in S[B:D]:
        print("Yes")
    else:
        print("No")
if C>D:
    if "##" not in S[A:C] and  "##" not in S[B:D]:
        if "..." in S[B-2:D+1]:
            print("Yes")
        else:
            print("No")
    else:
            print("No")
