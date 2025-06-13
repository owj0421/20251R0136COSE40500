import sys

n = int(sys.stdin.readline().strip())

if n < 1:
    print(0)
    
else:
    s = 1
    for i in range(n):
        s += (int(sys.stdin.readline().strip()) - 1)

    print(s)