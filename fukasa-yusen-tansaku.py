#深さ優先探索の練習
#木構造での
#ページ128
# 0-14までの各要素について、それぞれつながってる要素を記載
# 行きがけ順
tree=[[1,2],[3,4],[5,6],[7,8],[9,10],[11,12],[13,14],[],[],[],[],[],[],[],[]]

def search(pos):
    print(pos)
    for i in tree[pos]:
        search(i)
search(0)


