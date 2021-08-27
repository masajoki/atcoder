#ゴールから最適な行動を逆に選んでいく。
#最適な行動とは、相手との得点差を最大にする
#こういうのをミニマックス法というらしい。
#(h+w)%2==0なら高橋くんの手番
# 以下参考にした。
#https://atcoder.jp/contests/abc201/submissions/22650185

H,W=map(int,input().split())
#配列を2つに分けているが一つのほうが簡単

Tak = [[0] * W for _ in range(H)] #高橋のリードしている点数
Ao  = [[0] * W for _ in range(H)] #青木のリードしている点数
A=[]

for _ in range(H):
    T=input()
    U=[]
    for t in T:
        if t=='-':
            U.append(-1)
        else:
            U.append(1)
    A.append(U)

for i in range(H-1,-1,-1):
    for j in range(W-1,-1,-1):
        if (i+j)%2==0: #高橋の番
            if H >i+1>=0 and W>j+1>=0:
                #移動先でより高橋が勝っているマスを選ぶ
                Tak[i][j]=max(A[i+1][j]-Ao[i+1][j], A[i][j+1]-Ao[i][j+1]) 
            elif H >i+1>=0:
                Tak[i][j]=A[i+1][j]-Ao[i+1][j]
            elif W>j+1>=0:
                Tak[i][j]=A[i][j+1]-Ao[i][j+1] 
 
        if (i+j)%2==1: #Aokiの番
            if H >i+1>=0 and W>j+1>=0:
                #移動先でよりアオキが勝っているマスを選ぶ
                Ao[i][j]=max(A[i+1][j]-Tak[i+1][j], A[i][j+1]-Tak[i][j+1]) 
            elif H >i+1>=0:
                Ao[i][j]=A[i+1][j]-Tak[i+1][j]
            elif W>j+1>=0:
                Ao[i][j]=A[i][j+1]-Tak[i][j+1] 
 
if Tak[0][0]>0:
    print("Takahashi")
elif Tak[0][0]==0:
    print("Draw")
else:
    print("Aoki")
