# アルゴリズムの本 p222

# 1. 始点の到達コストをゼロにする
# 2. それ以外の点の到達コストを∞にする
# 3. 未確定の点の中から、最も小さい値をもつ地点を一つ選んで確定し記録する
# 4. 確定した点(a)から、直接つながり、かつ未確定な点(b)に対して以下を行う
#     1. aからそのbへの到達コスト（cost-a + cost-a:b < cost-b)が、bへの現コストよりも低かったら、cost-a+cost-a:bでcost-bを上書きする
# 5. すべての地点が確定していなければ3に戻る。

def dijkstra(edges,num_v):
    dist=[float('inf')]*num_v #各点の始点[0]からの距離
    dist[0]=0 
    q=[i for i in range(num_v)] #確定させるための記録簿として。 例では0~6まで。

    while len(q) > 0: #すべての地点が確定していなければ

        r=q[0] #確定していない地点を取り出す
        for i in q: #このループはコストが最小のものを取り出してるだけ
            if dist[i] < dist[r]:
                r=i 
        #r に最小のコストを持つ地点番号が入る

        u=q.pop(q.index(r)) #rを持つ要素のインデックス番号を指定してpop（取り出してい削除）

        for i in edges[u]: #i[0]は経路の到達点、dist[i[0]]は経路の到達点のコスト
            #経路の到達点のコストが、始点のコスト＋到達するコストi[1]より高ければ、到達点のコストを上書き
            if dist[i[0]] > dist[u]+i[1]:
                dist[i[0]]=dist[u]+i[1]

    return dist

edges=[ #接続先の地点、コスト
    [[1,4],[2,3]],  #点0から点１と点2へ、それぞれコスト4と3
    [[2,1],[3,1],[4,5]], #点1から点2,3,4へ、それぞれコスト1,1,5
    [[5,2]], 
    [[4,3]],
    [[6,2]],
    [[4,1],[6,4]],
    []
]

print(dijkstra(edges,7))