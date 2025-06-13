import sys

n = int(sys.stdin.readline())

for i in range(n):
    # n_blanks = n - i - 1
    num = 1 + i
    print('*' * num)
for i in range(n - 2, -1, -1):
    # n_blanks = n - i - 1
    num = 1 + i
    print('*' * num)