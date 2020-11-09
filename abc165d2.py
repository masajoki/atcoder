#floor(A*x/B)-A*floor(x/B)
# = (A*x-A*x%B)/B - A*(x-x%B)/B
# = ( (Ax - Ax%B) - Ax + A(x%B) )/B
# = (     - Ax%B      + A(x%B) )/B
# = (     - A(x%B)%B      + A(x%B) )/B

A,B,N=map(int,input().split())

