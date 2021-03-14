N=int(input())
numbers=[]
def stgs(s,l):
    global numbers
    if len(s)==l:
        numbers.append(s)
        return
    for t in ("3","5","7"):
        S=s+t
        stgs(S,l)

for n in range(1,1+len(str(N))):
    stgs("",n)

ans=0
for s in numbers:
    if '3' in s and '5' in s and '7' in s:
        if int(s)<=N:
            ans+=1

print(ans)
