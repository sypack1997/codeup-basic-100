a = int(input())
c = 1
s = 0

while True:
    s += c
    c += 1
    if s>=a:
        break
print(s)