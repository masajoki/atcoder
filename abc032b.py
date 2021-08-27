S=input()
k=int(input())
keys=set()
if k<=len(S):
    for i in range(len(S)-k+1):
        keys.add(S[i:i+k])

# print(keys)
print(len(keys))
