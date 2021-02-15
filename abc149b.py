A,B,K=map(int,input().split())

tempTAK=A-K
ansTAK=max(tempTAK,0)
tempAOK=B+min(ansTAK,tempTAK)
print(ansTAK,tempAOK)