import math
L=int(input())
ans=0
ans=math.factorial(L-1)//(math.factorial(11)*math.factorial(L-1-11))
print(int(ans))
