N=int(input())
S=list(input())
if N%2==1:
    print("No")
else:
    left= S[:len(S)//2] 
    right= S[len(S)//2:] 
    if left==right: 
        print("Yes")
    else:
        print("No")