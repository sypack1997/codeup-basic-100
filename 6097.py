h,w = map(int,input().split())
n = int(input())

hw = [[0 for j in range(w)]for i in range(h)]

for i in range(n):
    l,d,x,y = map(int, input().split())

    for j in range(l):
        if d == 0:
            hw[x-1][y+j-1] = 1
        else :
            hw[x+j-1][y-1] = 1

for i in range(h):
    for j in range(w):
        print(hw[i][j], end = ' ')
    print()