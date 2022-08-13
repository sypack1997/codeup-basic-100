a,m,d,n = input().split()
a = int(a)
d = int(d)
n = int(n)
m = int(m)

s = a
for i in range(2, n+1):
    s = s * m + d
print(s)