import sys
from collections import deque,defaultdict

N,M = tuple(map(int,sys.stdin.readline().strip().split()))
no_hear = set()
no_see = set()

for _ in range(N):
    no_hear.add(sys.stdin.readline().strip())

for _ in range(M):
    no_see.add(sys.stdin.readline().strip())

union = sorted(no_see&no_hear)
sys.stdout.write(str(len(union))+"\n")
sys.stdout.write("\n".join(union))
