B,C=map(int,input().split())

nums=0
if B==0:
    range1=[B-C//2,B]
    range2=[-B-(C-1)//2,-B]
    nums=range1[1]-range1[0]+1
    nums+=range2[1]-range2[0]
    print(nums)
    exit()

if B>0:

    range1=[B-C//2,B]
    range2=[-B-(C-1)//2,-B]
    range3=[B,(C-2)//2+B]
    nums=range1[1]-range1[0]+1
    if range1[0]<range2[1]:
        nums+=range1[0]-range2[0]
    else:
        nums+=range2[1]-range2[0]+1
    nums+=range3[1]-range3[0]
    print(nums)

if B<0:
    range1=[B-C//2,B]
    range2=[-B-(C-1)//2,-B]
    range3=[B,(C-2)//2+B]
    nums=range1[1]-range1[0]+1
    if range1[1]>range2[0]:
        nums+=range2[1]-range1[1]
    else:
        nums+=range2[1]-range2[0]+1
    nums+=range3[1]-range3[0]
    print(nums)