#10進数から26進数への変換
num=int(input())
def num2alpha(num):
    if num<=26:
        return chr(96+num)
    elif num%26==0:
        return num2alpha(num//26-1)+chr(122)
    else:
        return num2alpha(num//26)+chr(96+num%26)
print(num2alpha(num))