a = input()
b = input().split(' ')
nums=[int(i) for i in b]
divide_count=0
while True:
  for index,num in enumerate(nums):
    if int(num)%2==1:
      print(divide_count)
      exit()
    else:
      nums[index]=num/2
  divide_count +=1

