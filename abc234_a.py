#abc234_a.py
t=int(input())
def func(a):
    return a**2 + 2*a + 3

temp=func(func(func(t)+t)+func(func(t)))
print(temp)