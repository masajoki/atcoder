#import sys


#a = int(sys.argv[1])
#b = int(sys.argv[2])

a=input().split(' ')

if int(a[0])*int(a[1])%2 == 0:
  print('Even')
else:
  print('Odd')


