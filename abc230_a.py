N=int(input())
t=""
if N<=41:
    t=str(N).zfill(3)
else:
    t=str(N+1).zfill(3)

ans="AGC"+t
print(ans)
