vals=input().split(' ')
N=int(vals[0])
Y=int(vals[1])

for s in range(N,-1,-1):
  for m in range(N-s,-1,-1):
    l=N-s-m
    if l*10000+5000*m+1000*s == Y:
      print (l,m,s)
      exit()
print (-1,-1,-1)
