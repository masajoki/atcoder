N=int(input())
t=[]
x=[]
y=[]
#t.append(0)
#x.append(0)
#y.append(0)
t_cur=0
x_cur=0
y_cur=0

for i in range(N):
  plan=input().split(' ')
  t.append(int(plan[0]))
  x.append(int(plan[1]))
  y.append(int(plan[2]))

for i in range(N):
  t_gap=t[i]-t_cur
  x_gap=abs(x[i]-x_cur)
  y_gap=abs(y[i]-y_cur)

  dist=x_gap+y_gap

#  print("trip=",t[i],x[i],y[i])
#  print("t_gap=",t_gap)
#  print("dist=",dist)
  if (t_gap-dist)>=0 and (t_gap-dist)%2==0:
    t_cur=t[i]
    x_cur=x[i]
    y_cur=y[i]
  else:
    print("No")
    exit()
print("Yes")
