import sys

n = int(sys.stdin.readline().strip())
for i in range(n):
    n_stars = (n - i) * 2 - 1
    n_blanks = i
    print(' ' * n_blanks + '*' * n_stars)
    
for i in range(n-2, -1, -1):
    n_stars = (n - i) * 2 - 1
    n_blanks = i
    print(' ' * n_blanks + '*' * n_stars)