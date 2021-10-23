N,X=map(int,input().split())
A=list(map(int,input().split()))
def func(i,j):
    #i=N, j=X を初期値として始める。減らす方向で関数を動かす。
    # iを1ずつ減らして再帰させる
    # jとしてj-A[i-1]とjの両方で関数を呼び出す
    # i==0 でj==0になるならその組み合わせはある
    # 2**Nの組み合わせになりそう

    if i==0:
        if j==0:
            return True
        else:
            return False
    else:
        flag=False        
        if j>=A[i-1] and func(i-1,j-A[i-1])==True: #A[i-1]を選ぶ 
            flag=True
        elif func(i-1,j)==True: #A[i-1]を選ばない
            flag=True
        return flag

if func(N,X)==True:
    print("Yes")
else:
    print("No")

