N=int(input())
S=input()
T=""
for s in S:
    T=T.replace(s,"")
    T=T+s

print(T)
