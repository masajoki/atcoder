from typing import Counter


S=input()
c=Counter(S)
t=len(c)
if t==1:
    print(1)
elif t==2:
    print(3)
elif t==3:
    print(6)
