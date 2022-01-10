N=int(input())
Preorder=list(map(int,input().split()))
Inorder=list(map(int,input().split()))


def postorder(root):
    mid=Inorder.index(root)
    postorder(mid)

for p in P:
