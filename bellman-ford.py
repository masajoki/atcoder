def bellman_ford(edges,num_v):
    dist=[float('inf') for i in range(num_v)] #Infinityで各点までのコストを初期化
    dist[0]=0

    changed=True
    while changed:
        changed=False
        for edge in edges: #変更対象がなくなるまで辺について繰り返し
            if dist[edge[1]] > dist[edge[0]]+edge[2]: #この道を通ったほうが近ければ、この道を通っていく（終点のコストを小さくする）
                #頂点までのコストが更新できれば更新
                dist[edge[1]]=dist[edge[0]] + edge[2] #道の終点のコストを更新する
                changed=True
    return dist

#辺のリスト (起点、終点、コスト として記載)
edges = [
    [0,1,4],[0,2,3],[1,2,1],[1,3,1],[1,4,3],[2,5,2],[4,6,2],[5,4,1],[5,6,4]
]

print(bellman_ford(edges,7))