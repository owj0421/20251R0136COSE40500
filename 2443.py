import sys

n = int(sys.stdin.readline().strip())
for i in range(n):
    num = 1 + 2 * ((n - i) - 1)
    print(' ' * i + '*' * num)