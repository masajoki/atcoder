# 1周Kメートルの円
# 周りにN軒の家
# i番目の家は円の北端から時計回りにAiメートル
# いずれかの家から出発してN軒すべての家を尋ねるための最短移動距離は？

K,N=map(int,input().split())
A=list(map(int,input().split()))
An2A1=A[0]+K-A[-1]
gaps=[An2A1]
for i in range(1,N):
    gaps.append(A[i]-A[i-1])

print(K-max(gaps))
