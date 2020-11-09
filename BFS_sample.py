#幅優先探索の勉強
# https://nashidos.hatenablog.com/entry/2020/01/14/110011
 
# サンプル問題
# https://atcoder.jp/contests/atc001/tasks/dfs_a
# この問題は深さ優先でも幅優先でも解けるので、幅優先で解いていく

H,W=map(int,input().split())
C=list(list(input()) for i in range(H)]

queue=[] # queueという名前だがこれはリスト


#スタート地点をさがしてqueueに入れる。
# visitedにも入れる

for i in range(H):
    for j in range(W):
        if(C[i][j] == 's':
            queue.append([i,j])
            visited[i][j]=1

# これは、行ける方向かな
dy_dx=[[1,0],[0,1],[-1,0][0,-1]]


while len(queue) > 0:
    now = queue.pop(0) #指定した位置の要素を削除し、値を取得: pop()→つまり左から取る。最初に入れたものを取って消す。
    if　C[now[0]][now[1]]=='g':
        print('Yes')
        exit()
    for i in range(4):
        # now[0]はqueueから取り出した位置[x,y]のy、dy_dx[i][0] は 4方向ある1方向のy移動幅
        # now[1]はqueueから取り出した位置[x,y]のx、dy_dx[i][1] は 4方向ある1方向のx移動幅
        # x,y は今から次に行く場所
        y = now[0]+dy_dx[i][0] 
        x = now[1]+dy_dx[i][1] 
        if 0 <= y < H and 0 <= x < W: 
            if C[y][x] != '#' and visited[y][x]== 0: # 壁でなく、行ったことがない場所である（行ったことがある場所には行かない）
                visited[y][x]=1 #行ったことにする
                queue.append([y,x]) #

print('No')