#abc233_e.py
#大きい数字は文字列として扱う
#筆算するような感じで解いている。
# 314159
#  31415
#   3141
#    314
#     31
#      3

# 累積和みたいにして考える

X=input()
S=[0 for _ in range(len(X)+1)]

for i in range(1,len(X)+1):
    S[i]=S[i-1]+int(X[i-1])
    
ans=[]

for i in range(len(S)-1,0,-1):
    ans.append(S[i]%10) #1桁目を取り出してる
    S[i-1]+=S[i]//10 #2桁目以降

if S[0]!=0: #桁上りしている場合
    ans.append(S[0])

ans.reverse()
for a in ans:
    print(a,end="")
print()