import itertools
AB=["a","b","c","d","e"]

for i in range(2**len(AB)):
    t=""
    for j in range(len(AB)):
        if i>>j&1:
            t=t+"1"+AB[j]
        else:
            t=t+"0"+AB[j]
        if j<len(AB)-1:
            t=t+"+"
    if i<2**len(AB)-1:
        print(t)
    else:
        print(t)

