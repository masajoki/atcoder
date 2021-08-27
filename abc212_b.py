T=list(input())
a,b,c,d=map(int,T)
X=[a,b,c,d]

if a==b==c==d:
    print("Weak")
    exit()


for i in range(1,4):
    if X[i-1]+1==X[i] or  X[i-1]==9 and X[i]==0:
        continue
    else:
        print("Strong")
        exit()
print("Weak")