w,h,b = input().split()
w = int(w)
h = int(h)
b = int(b)

b = b / 8 / 1024 / 1024

print(format(w * h * b, ".2f"), "MB")