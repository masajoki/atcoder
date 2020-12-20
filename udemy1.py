x=[1,2,3]
y=[2,3.9,6.1]

bunshi=0
bunbo=0
for i in range(3):
    bunshi+=x[i]*y[i]
    bunbo+=x[i]**2

print(bunshi/bunbo)
33333