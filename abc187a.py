A,B=map(int,input().split())
a=list(map(int,list(str(A))))
b=list(map(int,list(str(B))))

print(max(sum(a),sum(b)))