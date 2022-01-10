import itertools
L = list(range(1,7)) #[1,2,3,4,5,6]
AC = list(itertools.accumulate(L))+[0] #[1,3,6,10,15,21,0]
#要素の1つ目から5つ目の合計が知りたい場合の書き方(1+2+3+4+5=15)
l,r=0,4
print(AC[r]-AC[l-1])# 15 (AC[4]-AC[-1]→15-0→15)
