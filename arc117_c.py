import sys
sys.setrecursionlimit(10**7) 
N=int(input())
A=input()
fours=[]

for i in range(1,10):
    fours.append(4**i)

def solve(S):
    if len(S)==1:
        return(S[0])
    elif len(S) in fours:
        if S[0]==S[-1]:
            return(S[0])
        elif "B" not in (S[0],S[-1]):
            return("B") 
        elif "W" not in (S[0],S[-1]):
            return("W") 
        elif "R" not in (S[0],S[-1]):
            return("R")

    T=[]
    for i in range(len(S)-1):
        if S[i]==S[i+1]:
            T.append(S[i])
        elif "B" not in (S[i],S[i+1]):
            T.append("B") 
        elif "W" not in (S[i],S[i+1]):
            T.append("W") 
        elif "R" not in (S[i],S[i+1]):
            T.append("R")
    return solve(T)

print(solve(A))


