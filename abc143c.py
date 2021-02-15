# N 匹のスライムが横一列に並んでいます
# これらの色に関する情報が、長さ N の英小文字から成る文字列 S で与えられます
# 左から i 番目のスライムは、 S の i 文字目に対応する色を持っています
# 同じ色を持ち隣接するスライムは融合し、色は変わらずに 1 匹のスライムとなります
# このとき、融合した後のスライムは、融合する前の各スライムが隣接していた他のスライムと隣接した状態になります
# 最終的に存在するスライムは何匹となるでしょうか
N=int(input())
S=list(input())
ans=0
last=''
for s in S:
    if s!=last:
        ans+=1
    last=s
print(ans)