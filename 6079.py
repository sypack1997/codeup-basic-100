a = int(input())
b = 0

for i in range(1, a+1):
    b = b + i
    if a <= b:
        print(i)
        break


# codeup answer
n = int(input())

s = 0
t = 0
while s<n:
    t = t+1
    s = s+t

print(t)