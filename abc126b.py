S=input()
# SI=list(map(int,S))
# print(SI)
aa=int(S[0]+S[1])
bb=int(S[2]+S[3])
if (aa==0 or aa >12) and 1<= bb <= 12:
    print("YYMM") 
elif  1<= aa <=12 and (bb==0 or bb >12): 
    print("MMYY")
elif 1<=aa <=12 and 1<=bb<=12:
    print("AMBIGUOUS")
else:
    print("NA")