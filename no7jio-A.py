# https://atcoder.jp/contests/joi2008yo/tasks/joi2008yo_a

P=int(input())
R=1000-P
ans=0


def maxOtsuri(c):
    global R,ans
    if R//c >0:
        ans+=R//c
        R=R-(R//c)*c


coins=[500,100,50,10,5,1]
for c in coins:
    maxOtsuri(c)

print(ans)