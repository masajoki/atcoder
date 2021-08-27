S=list(input())
ans=0
multiple=False
nonzero=False
multipliedbyzero=False
zero=False
for s in S:
    if s=="0":
        zero=True
        if multiple:
            multipliedbyzero=True
    elif s in [str(i) for i in range(1,10)]:
        nonzero=True
    elif s=="+":
        if nonzero and not multipliedbyzero:
            ans+=1
        nonzero=False
        zero=False
        multipliedbyzero=False
        multiple=False
    elif s=="*":
        multiple=True
        if zero:
            multipliedbyzero=True
if nonzero and not multipliedbyzero:
    ans+=1
print(ans)
