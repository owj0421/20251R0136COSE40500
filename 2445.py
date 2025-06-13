import sys

n = int(sys.stdin.readline().strip())
for i in range(n):
    n_blanks = (n - i - 1) * 2
    n_stars = i + 1
    print('*' * n_stars + ' ' * n_blanks + '*' * n_stars)
    
for i in range(n-2, -1, -1):
    n_blanks = (n - i - 1) * 2
    n_stars = i + 1
    print('*' * n_stars + ' ' * n_blanks + '*' * n_stars)