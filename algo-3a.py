s=input()
t=input()
if s==t:
    print('same')
else:
    sl=s.lower()
    tl=t.lower()
    if sl==tl:
        print('insensitive')
    else:
        print('different')

