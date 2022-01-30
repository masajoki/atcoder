#アルゴ式.平均値.py
import statistics
N=int(input())
A=list(map(int,input().split()))
# print(sum(A)/N)
print(statistics.mean(A))