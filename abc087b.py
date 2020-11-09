A=input()
B=input()
C=input()
X=input()
x=int(X)
count=0
for a in range(int(A)+1):
  for b in range(int(B)+1):
    for c in range(int(C)+1):
      if x-a*500-b*100-c*50==0:
        count+=1
print(count)
