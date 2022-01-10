import math
print(math.pi)
print(math.sqrt(2))
c=2.99792458E8
print(c)
na=6.02214076E23
print(na)

a="あああ{0:12.8g} いいい {1:025.3f}"
s=a.format(c,na)
print(type(s))

print(a.format(c,na))


def finf(s="デフォルト引数"):
    print(" finf called. with %s" % (s))

def F(f):
    print(" F called and ...", end="")
    f("渡された引数")

finf()
F(finf)

print("%f %d %s" % (2,1.111111,"aaa"))