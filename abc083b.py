vals=input().split(' ')
N=int(vals[0])
A=int(vals[1])
B=int(vals[2])

total=0

number=1
while number<=N:
  subtotal=0
  for n in str(number):
    subtotal+=int(n)
  if A<= subtotal & subtotal <= B:
    total+=number
  number+=1

print(total)
