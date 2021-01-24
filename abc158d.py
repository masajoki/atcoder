S=input()
Q=int(input())
reversed=False
for i in range(Q):
    q=list(input().split())
    if q[0]=='1':
        reversed= not(reversed)
    else:
        if q[1]=='1':
            if reversed:
                S=S+q[2]
            else:
                S=q[2]+S
        else:
            if reversed:
                S=q[2]+S
            else:
                S=S+q[2]
if reversed:
    temp=list(S)
    temp.reverse()
    print(''.join(temp))
else:
    print(S)