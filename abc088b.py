N=int(input())
a_input_list=input().split(' ')
a_num_list=[]
for a in a_input_list:
  a_num_list.append(int(a))

a_num_list.sort()
a_num_list.reverse()

bob=0
allice=0

counter=0
for a in a_num_list:
  if counter%2==0:
    allice+=a
  else:
    bob+=a
  counter+=1

print(allice-bob)

