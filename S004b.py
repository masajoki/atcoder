from collections import deque
A=input()
B=input()
S=input()

Q=deque()

starta=(0,0,0,0,1) # 0:a,1:b ,  a/bの位置, sの位置, cost) 
startb=(1,0,0,0,1) # 0:a,1:b ,  a/bの位置, sの位置, cost)  


Q.append(starta)
Q.append(startb)

apos=0
bpos=0
anscost=[]
while len(Q)>0:
    ab,apos,bpos,spos,cost=Q.popleft()
    if ab==0:
        if apos<len(A):                
            if A[apos]==S[spos]:
                if spos==len(S)-1:
                    anscost.append(cost)
                else:
                    Q.append((0,apos+1,bpos,spos+1,cost+1))
                    Q.append((1,apos,bpos+1,spos+1,cost+1))
            else:
                Q.append((0,apos+1,bpos,spos,cost+1))
    if ab==1:
        if bpos<len(B):
            if B[bpos]==S[spos]:
                if spos==len(S)-1:
                    anscost.append(cost)
                else:
                    Q.append((0,apos+1,bpos,spos+1,cost+1))
                    Q.append((1,apos,bpos+1,spos+1,cost+1))
            else:
                Q.append((1,apos,bpos+1,spos,cost+1))

pass