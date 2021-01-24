sx,sy,tx,ty=map(int,input().split())
h=ty-sy
w=tx-sx
print(h*"U"+w*"R"+h*"D"+w*"L",end="")
print("L"+(h+1)*"U"+(w+1)*"R"+"D"+"R"+(h+1)*"D"+(w+1)*"L"+"U")
