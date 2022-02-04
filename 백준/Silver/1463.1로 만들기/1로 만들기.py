import sys
import math
from collections import deque
X = int(sys.stdin.readline().strip())

memo = [0 for i in range(X+1)]
try:
    memo[2] = 1
except:
    pass
try:
    memo[3] = 1
except:
    pass

if X > 3:
    for i in range(4,X+1):

        memo[i] = memo[i-1]+1

        if i % 3 == 0:
            memo[i] = min(memo[i],memo[i // 3]+1)

        if i % 2 == 0:
            memo[i] = min(memo[i], memo[i // 2]+1)

sys.stdout.write(str(memo[X]))