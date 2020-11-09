#DFS_sample.py
#解説 https://nashidos.hatenablog.com/entry/2020/01/04/234842
#サンプル問題
# https://atcoder.jp/contests/atc001/tasks/dfs_a
# 幅500、高さ500
# 道を東西南北に移動できますが斜めには移動できません。 また、塀の区画は通ることができません。
# 
#  s : その区画が家であることを表す。
#  g : その区画が魚屋であることを表す。
#  . : その区画が道であることを表す。
#  # : その区画が塀であることを表す。
# 
# sからgにたどり着けるか

import sys
sys.setrecursionlimit(10**7) #スタックオーバーフローを防ぐため再帰呼び出しを1000万回に制限

H,W=map(int,input().split())
c=list(list(input()) for i in range(H)) #リストが二重になっているっぽいのはなんでだろう？→文字列をリストに分割してる
# print(c)

def dfs(h,w):  #h: height, w: width
    #壁にあたった、範囲外に出た場合 (xを縦、yを横で考えているが変かな？)
    if not ( 0<=h < H) or not ( 0 <= w < W) or c[h][w]=="#": 
        return
    if c[h][w] == "g": #ゴール
        print("Yes")
        exit()
    c[h][w]="#"
    dfs(h+1,w)
    dfs(h-1,w)
    dfs(h,w+1)
    dfs(h,w-1)

for i in range(H):
    for j in range(W):
        if c[i-1][j-1]=="s":
            sh,sw=i,j
dfs(sh,sw)
print('No')