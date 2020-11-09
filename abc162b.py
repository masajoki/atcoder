#ABC162B B - FizzBuzz Sum
# iが3でも5でも割り切れる ai=FizzBuz
# iが3で割り切れる ai=Fizz
# iが5で割り切れる ai=Buzz
# 割り切れない ai=i

# 1<=N<=10**6
N=int(input())
A=[]
for i in range(N+2):
    A.append(i)
for i in range(N//3+1):
    A[i*3]=0
for i in range(N//5+1):
    A[i*5]=0
ans=0
for i in range(N+1):
    ans+=A[i]
print(ans)