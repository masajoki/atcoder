S=list(input())
T=list(input())
win=True
atcoder=list("atcoder")
for i in range(len(S)):
    s=S[i]
    t=T[i]
    if s==t:
        pass
    elif (s=='@' and t in atcoder ) or  (t=='@' and s in atcoder ):
        pass
    else:
        print ("You will lose")
        exit()
print("You can win")


