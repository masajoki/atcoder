n=int(input())
N=n**2
if n==1:
    print(1)
    print("AB")
    exit()

for i in range(N):
    fmt="0"+str(N)+"b"
    s=format(i,fmt)
    if s.count("1")==s.count("0"):
        # print(s)
        s2=s.replace("0","A").replace("1","B")
        print(s2)
