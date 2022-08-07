a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
d = 0

for i in range(0, a):
    for j in range(0, b):
        for k in range(0, c):
            d = d + 1
            print(i,j,k)
print(d)



# codeup answer
r, g, b = input().split()

r = int(r)
g = int(g)
b = int(b)

for i in range(0, r) :
  for j in range(0, g) :
    for k in range(0, b) :
      print(i, j, k)

print(r*g*b)