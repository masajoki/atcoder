#桁ごとに単調に増加していくような数列を再帰で作るサンプル
#深さ優先探索を再帰で実装してる

A=[]
max=1 #各桁をいくつまで数字を増やすか
digits=3 #桁数

def dfs(start):
    if len(A)==digits:
        print("".join(A)) #
        return
    for i in range(start,max+1):
        A.append(str(i))
        dfs(i)
        A.pop()
dfs(0)