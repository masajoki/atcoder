import sqlite3
N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
con = sqlite3.connect(':memory:', isolation_level=None)
cur = con.cursor()
cur.executescript("""
PRAGMA trusted_schema = OFF;
PRAGMA journal_mode = OFF;
PRAGMA synchronous = OFF;
PRAGMA temp_store = memory;
PRAGMA secure_delete = OFF;

CREATE TABLE presents (aid INT,takahashi INT, aoki INT);
CREATE INDEX preindex1 ON presents(aid,takahashi, aoki);
CREATE INDEX preindex2 ON presents(takahashi, aoki);
CREATE INDEX preindex3 ON presents(aoki);

""")
cur.execute("begin")
for i in range(N):
    a=A[i]
    b=B[i]
    cur.execute("INSERT INTO presents VALUES(?,?, ?)", (i,a, b))

ans=N
for i in range(N):
    a=A[i]
    b=B[i]
    cur.execute("select count(*) from presents where takahashi <=? and aoki >= ? and aid != ?", (a, b, i))
    temp=cur.fetchall()
    ans+=temp[0][0]
print(ans)
