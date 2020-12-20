#締切の厳しいのからやっていって入れば入るし入らなければ入らないのでは？
N=int(input())
BA=[]
for _ in range(N):
    a,b=map(int,input().split())
    BA.append([b,a])
BA.sort()
today=0
for ba in BA:
    today+=ba[1]
    if today>ba[0]:
        print("No")
        exit()
print("Yes")