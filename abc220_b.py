K=int(input())
A,B=input().split()

def calc(I):
    It=0
    for i in range(len(I)):
        It+=(K**(len(I)-i-1))*int(I[i])
    return It

print(calc(A)*calc(B))



