#アルゴ式.データ間の関係性 1.py
import statistics
from telnetlib import BM
N=input()
A=list(map(int,input().split()))
B=list(map(int,input().split()))
Amean=statistics.mean(A)
Bmean=statistics.mean(B)

print(min(Amean,Bmean)/max(Amean,Bmean))