# Unification
import collections
from typing import Counter
S=list(input())
c=Counter(S)
# print(c)
print(min(c['0'],c['1'])*2)