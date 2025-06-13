import sys

n = int(sys.stdin.readline().strip())

for i in range(n):
    n_blanks = n - i - 1
    num = 1 + i
    print(' ' * n_blanks + '*' * num)
for i in range(n - 2, -1, -1):
    n_blanks = n - i - 1
    num = 1 + i
    print(' ' * n_blanks + '*' * num)