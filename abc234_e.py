#abc234_e.py
X=input()
xlen=len(X)
ans=10**19
for k in range(10):
    for i in range(-9,10):
        A=[]
        x=(int(X[0])+k)%10
        A.append(str(x))
        for j in range(1,xlen):
            t=int(A[j-1])
            if t+i<0 or t+i>9:
                break
            a=str((t+i)%10) 
            A.append(a)
        Ai=int("".join(A))
        # print(Ai)
        if Ai >= int(X):
            ans=min(ans,Ai)

print(ans)

