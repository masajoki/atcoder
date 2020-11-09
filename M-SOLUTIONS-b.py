"""
整数 A が書かれた赤のカード
整数 B が書かれた緑のカード
整数 C が書かれた青のカード

以下の操作を 
K 回まで行うことができます。

3 枚のうちいずれか 
1 枚のカードを選び、書かれた整数を 
2 倍する。

成功条件

B 緑のカードに書かれている整数> A 赤のカードに書かれている整数
C 青のカードに書かれている整数> B 緑のカードに書かれている整数
B > A
C > B

1 <= A,B,C <= 7
つまり
C > B > A

 """
A,B,C=map(int,input().split())
K=int(input())

magic=0

while A>=B and magic < K:
    B*=2
    magic+=1

while B>=C and magic < K:
    C*=2
    magic+=1

if C > B > A:
    print("Yes")
else:
    print("No")