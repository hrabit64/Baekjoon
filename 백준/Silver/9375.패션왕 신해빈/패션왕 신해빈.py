import sys
from collections import defaultdict

T = int(sys.stdin.readline().strip())

for _ in range(T):
    n = int(sys.stdin.readline().strip())
    items = defaultdict(int)
    for _ in range(n):
        _,cate = map(str,sys.stdin.readline().strip().split())
        items[cate] += 1

    res = 1
    for i in items.values():
        res = res*(i+1)

    sys.stdout.write(str(res-1)+"\n")

