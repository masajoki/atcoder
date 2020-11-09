K=int(input())
S=input()
slen=len(S)
if slen > K:
  print (S[0:K]+"...")
else:
  print (S)
