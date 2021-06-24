x,y=map(int,input().split())
if y==0:
    print("ERROR")
else:
    ans='{:.4f}'.format(x/y)
    print(ans[0:-2])
