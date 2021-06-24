A=list(map(int,input().split()))
maxi=A.index(max(A))
mini=A.index(min(A))
for i in range(3):
    if i not in (mini,maxi):
        if i==0:
            print("A")
        elif i==1:
            print("B")
        else:
            print("C")
