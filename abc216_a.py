A=input()
a=A[-1]
ai=int(a)
if 0<=ai<=2:
    print(A[:-2]+"-")

elif 3<=ai<=6:
    print(A[:-2])
elif 7<=ai<=9:
    print(A[:-2]+"+")