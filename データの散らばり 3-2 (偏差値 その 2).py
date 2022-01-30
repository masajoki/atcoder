#データの散らばり 3-2 (偏差値 その 2).py
import statistics
N=int(input())
A=list(map(int,input().split()))
av=statistics.mean(A)
sd=statistics.pstdev(A)
T=[50+10*(a-av)/sd for a in A]
print(T[0])