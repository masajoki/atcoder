A,B,T=map(int,input().split())

b=0
sec=0
for i in range(1,100):
    sec=A*i
    if sec < T+0.5:
        b+=B
    else:
        break
print(b)
