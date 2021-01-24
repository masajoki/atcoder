from collections import deque
Sa=input()
Sb=input()
Sc=input()
SaQ=deque()
SbQ=deque()
ScQ=deque()

for s in Sa:
    SaQ.append(s)

for s in Sb:
    SbQ.append(s)

for s in Sc:
    ScQ.append(s)

t=SaQ.popleft()
while True:
    if t=='a':
        if len(SaQ)>0:
            t=SaQ.popleft()
        else:
            print("A")
            break
    elif t=='b':
        if len(SbQ)>0:
            t=SbQ.popleft()
        else:
            print("B")
            break
    else:
        if len(ScQ)>0:
            t=ScQ.popleft()
        else:
            print("C")
            break

