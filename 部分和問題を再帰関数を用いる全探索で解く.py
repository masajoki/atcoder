N,W=map(int,input().split())
A=list(map(int,input().split()))

def func (i,w,a,history):
    print("func(i:",i,"w:",w,")")
    #ベースケース
    if i==0:
        if w == 0: 
            print("   return True")
            return True
        else:
            print("   return False")
            return False
    print("    アイテム",i-1,"を選ばない場合", history)    
    bool=func(i-1,w,a,history+str(i-1)+":x ")
    if bool:
        print( "  True:",history)
        return True

    print("    アイテムを",i-1,"選ぶ場合", history)
    bool=func(i-1,w-a[i-1],a,history+str(i-1)+":o ")
    if bool:
        print( "  True:",history)
        return True
    else:
        print( "  False:",history)
        return False

if func(N,W,A,""):
    print("YES")
else:
    print("NO")





