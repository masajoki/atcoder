N=int(input())
ans=""

m=N
for i in range(3,0,-1):
    t=m//(36**i)
    m=m%(36**i)
    if t==0 and ans!="":
        ans=ans+"0"
    elif 0<t<10:
        ans=ans+chr(48+t)
    elif 10<=t:
        ans=ans+chr(55+t)
m=m%36
if m<10:
    ans=ans+chr(48+m)
else:
    ans=ans+chr(55+m)

print(ans)

    

