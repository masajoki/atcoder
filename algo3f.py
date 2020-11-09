N=int(input())
A=[]
for _ in range(N):
    A.append(list(set(list(input() )))) #文字をソートして重複排除

kaibun=''
for i in range(N//2):
    found=False
    for a in A[i]:
        if a in A[N-i-1]:
            kaibun=kaibun+a
            found=True
            break
    if found==False:
        print(-1)
        exit()

kaibunrev=kaibun[::-1] #文字を逆順にする。文字列反転。
if N%2==1: #Nが奇数だったら真ん中の文字は先頭の文字にする
    kaibun=kaibun+A[N//2][0] 
    
print(kaibun+kaibunrev)
