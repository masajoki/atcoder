#こうやって値を入れて出力してみるとわかりやすい！
import math
A,B,N=map(int,input().split())
print("A=",A,"B=",B)
for x in range(1,100):
    temp=math.floor(A*x/B) - A*math.floor(x/B)
    print("x=",str(x),math.floor(A*x/B) ,A*math.floor(x/B),"ans=",temp)