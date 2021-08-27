N=3
last=0
count=0
for i in range(1000):
    s=format(bin(i))
    if s.count('1')==N:
        count+=1
        print(count,i,i-last,bin(i))
        last=i


