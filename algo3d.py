N=int(input())
S1=input()
S2=input()
S3=input()
S4=input()
S5=input()
ans=''

for i in range(0,N*4+1,4):
    temp=S1[i+1:i+4]+S2[i+1:i+4]+S3[i+1:i+4]+S4[i+1:i+4]+S5[i+1:i+4]
    if temp=='####.##.##.####':
        ans=ans+'0'
    elif temp=='.#.##..#..#.###':
        ans=ans+'1'
    elif temp=='###..#####..###':
        ans=ans+'2'
    elif temp=='###..####..####':
        ans=ans+'3'
    elif temp=='#.##.####..#..#':
        ans=ans+'4'
    elif temp=='####..###..####':
        ans=ans+'5'
    elif temp=='####..####.####':
        ans=ans+'6'
    elif temp=='###..#..#..#..#':
        ans=ans+'7'
    elif temp=='####.#####.####':
        ans=ans+'8'
    elif temp=='####.####..####':
        ans=ans+'9'

print(ans)