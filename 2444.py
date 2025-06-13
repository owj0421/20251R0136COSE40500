import sys

n = int(sys.stdin.readline().strip())
for i in range(n):
    num = 1 + 2 * i
    print(' ' * (n - i - 1) + '*' * num)

for i in range(n - 2, -1, -1):
    num = 1 + 2 * i
    print(' ' * (n - i - 1) + '*' * num)
