N,A,B=map(int,input().split())

minsum=A*(N-1)+B
maxsum=A+B*(N-1)
ans=maxsum-minsum+1
print(max(0,ans))

#最初は重複を許す組み合わせの計算を考えたが、よく考えたら単純だった