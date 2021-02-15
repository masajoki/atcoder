DAYS=["SUN","MON","TUE","WED","THU","FRI","SAT"]
S=input()
for i in range(len(DAYS)):
    s=DAYS[i]
    if S==s:
        print(7-i)
