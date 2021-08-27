S=input()
N=int(S)
np=False
if N==1:
    print("Not Prime")
    exit()

if N==2:
    print("Prime")
    exit()

if N%2==0:
    np=True

for i in range(3,min(N,int(N**0.5)+1),2):
    if N%i==0:
        np=True
        break

if np==False:
    print("Prime")
    exit()

if int(S[-1])%2==0 or S[-1]=="5":
    print("Not Prime")
    exit()
else:
    temp=0
    for s in S:
        temp+=int(s)
    if temp%3!=0:
        print("Prime")
    else:
        print("Not Prime")

