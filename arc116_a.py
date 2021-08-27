T=int(input())
case=[]
for i in range(T):
    case.append(int(input()))

for c in case:
    if c % 4 ==0:
        print("Even")
    elif c % 2 ==0:
        print("Same")
    else:
        print("Odd")
