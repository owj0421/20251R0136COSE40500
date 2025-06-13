import sys

format = "You get {0} piece(s) and your dad gets {1} piece(s)."
n = int(sys.stdin.readline().strip())
for _ in range(n):
    a, b = map(int, sys.stdin.readline().strip().split())
    print(format.format(a // b, a % b))