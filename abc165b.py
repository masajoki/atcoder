import math
X=int(input())
I=100
year=0
while True:
    year+=1
    I=(I*101//100)
    if I >= X:
        print(year)
        break
