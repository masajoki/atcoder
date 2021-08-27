S=input()

T=[]
for i in range(len(S)-1,-1,-1):
    t=S[i]
    if t=='6':
        t='9'

    elif t=='9':
        t='6'
    T.append(t)
Ts=   "".join(T) 
print(Ts)
