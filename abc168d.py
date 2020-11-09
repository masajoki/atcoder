from collections import deque
s=input().split(' ')
N=int(s[0])
M=int(s[1])
room_from=[]
room_to=[]
path=[]
for i in range(M):
  s=input().split(' ')

#道は両方向に使える
  room_from.append(int(s[0]))
  room_to.append(int(s[1]))
  room_from.append(int(s[1]))
  room_to.append(int(s[0]))

#for i in range(2*M):
#  print("from=",room_from[i],"to=",room_to[i])


#最小経路の回答を入れる. ansewr[room_from]=room_to


answer={}
todo={}
temp={}
todoq=Queue(N)

for (i,room) in enumerate(room_to): 
  if room_to[i] == 1:
    todo[room_from[i]]=1

answer.update(todo)

while True:
  for a in todo:
    for (i,room) in enumerate(room_to): 
      if room == a and room_from[i] not in temp and room_from[i] not in answer and room_from[i] != 1:
        temp[room_from[i]]=a
  if len(temp)==0:
    break
  else:
    todo.clear()
    todo.update(temp)
    answer.update(temp)
    temp.clear()
    print(answer)

print(answer)
if len(answer)== N-1 :
  print ("Yes")
  for n in answer:
    print (answer[n])
else:
  print ("No")


