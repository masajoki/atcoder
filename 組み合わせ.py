import itertools
#累積和
A=[1,2,3,4,5,6,7,8,9,20]
print(list(itertools.accumulate(A)))

#ある値が何個あるか
A=[1,1,1,2,2,33,3,3,100,4,5,6,7,8,9,1,2,3,20]
gr=itertools.groupby(A)
for key,group in gr:
    print(key,list(group))



#順列の例
print(list(itertools.permutations([1, 2, 3])))


#組み合わせの例
print(list(itertools.combinations([1, 2, 3], 2)))


#直積の例
print(list(itertools.product([0,1], repeat=4)))
print(list(itertools.product([0,1], repeat=4)))