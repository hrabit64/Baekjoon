import sys
from collections import deque




N = int(sys.stdin.readline().strip())
memo = [0 for _ in range(N+2)]
stairs = [0 for _ in range(N+2)]

for i in range(N):
    stairs[i] = int(sys.stdin.readline().strip())

memo[0] = stairs[0]
memo[1] = stairs[1] + stairs[0]
memo[2] = max(stairs[1] + stairs[2],stairs[2] + stairs[0])

for i in range(3,N):
    memo[i] = max(memo[i-3] + stairs[i-1] + stairs[i] ,  memo[i-2] + stairs[i])

sys.stdout.write(str(memo[N-1]))