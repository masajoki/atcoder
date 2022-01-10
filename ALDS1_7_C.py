from collections import deque
N=int(input())
Child=[[-1,-1] for _ in range(N)]
Parent=[-1]*N
for i in range(N):
    id,l,r=map(int,input().split())
    Child[id][0]=l
    Child[id][1]=r
    for rl in (r,l):
        if rl!=-1:
            Parent[rl]=id
    
# 根接点、左部分木、右部分木の純で接点の番号_________を出力する：先行順巡回
root=Parent.index(-1)

def preorder(id):
    print(" %d"%(id),end="")
    lid,rid=Child[id]
    if lid!=-1:
        preorder(lid)
    if rid!=-1:
        preorder(rid)

def inorder(id):
    lid,rid=Child[id]
    if lid!=-1:
        inorder(lid)
    print(" %d"%(id),end="")
    if rid!=-1:
        inorder(rid)

def postorder(id):
    lid,rid=Child[id]
    if lid!=-1:
        postorder(lid)
    if rid!=-1:
        postorder(rid)
    print(" %d"%(id),end="")

print("Preorder")
preorder(root)

print("\nInorder")
inorder(root)

print("\nPostorder")
postorder(root)
print()


