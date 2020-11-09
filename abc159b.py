s=list(input())
n=len(s)

candidate1 = s[:(n-1)//2]
candidate2 = s[(n+3)//2-1:]

def kaibunChedker(candidate1):
    for i in range(len(candidate1)//2+1):
        if candidate1[i]!=candidate1[-1-i]:
            print("No")
            exit()

kaibunChedker(s)
kaibunChedker(candidate1)
kaibunChedker(candidate2)
print("Yes")