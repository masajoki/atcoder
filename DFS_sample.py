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

h,w=map(int,input().split())
c=list(list(input()) for i in range(h)) #リストが二重になっているっぽいのはなんでだろう？→文字列をリストに分割してる
# print(c)

def dfs(y,x):
    #壁にあたった、範囲外に出た場合 (xを縦、yを横で考えているが変かな？)
    if not ( 0<=y < h) or not ( 0 <= x < w) or c[y][x]=="#": 
        return
    if c[y][x] == "g": #ゴール
        print("Yes")
        exit()
    c[y][x]="#"
    dfs(y+1,x)
    dfs(y-1,x)
    dfs(y,x+1)
    dfs(y,x-1)

for i in range(h):
    for j in range(w):
        if c[i-1][j-1]=="s":
            sy,sx=i,j
dfs(sy,sx)
print('No')