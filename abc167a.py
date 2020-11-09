#abc167a
#
import re
S=input()
T=input()
if T.find(S) == 0:
    if re.match('[a-z]',T[len(S)-1]):
        print("Yes")
else:
    print("No")
        