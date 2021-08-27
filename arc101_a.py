N,K=map(int,input().split())
X=list(map(int,input().split()))
firetime=0
for i in range(K-1):
    firetime+=X[i+1]-X[i]

firetime+=min(abs(X[0]),abs(X[K-1]))
minfiretime=firetime
for i in range(K,N):

    deduct=(X[i-K+1]-X[i-K])
    addition=(X[i]-X[i-1])
    laststartpoint=min(abs(X[i-K]),abs(X[i-1]))
    nextstartpoint=min(abs(X[i-K+1]),abs(X[i]))
    firetime=firetime-deduct+addition-laststartpoint+nextstartpoint
    minfiretime=min(minfiretime,firetime)
    
print(minfiretime)