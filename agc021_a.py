N=list(map(int,input()))
print(max(sum(N),N[0]-1+(len(N)-1)*9))