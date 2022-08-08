h,b,c,s = input().split()
h = int(h)
b = int(b)
c = int(c)
s = int(s)

s = s / 8 /1024 /1024
print(format(h*b*c*s, ".1f"),"MB")