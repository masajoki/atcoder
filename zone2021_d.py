from collections import deque
T=deque()
S=input()

reverse=False
for s in S:
    if s=='R':
        reverse = not reverse
        continue
    if reverse:
        if len(T)>0:
            t=T.popleft()
            if s!=t:
                T.appendleft(t)
                T.appendleft(s)
        else:
            T.appendleft(s)
    else:
        if len(T)>0:
            t=T.pop()
            if s!=t:
                T.append(t)
                T.append(s)
        else:
            T.append(s)

if  not reverse:
    for _ in range(len(T)):
        t=T.popleft()
        print(t,end="")    
else:
    for _ in range(len(T)):
        t=T.pop()
        print(t,end="")    
print()
