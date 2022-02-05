import sys
import math
from collections import deque

a = sys.stdin.readline().strip()
a = a.split("-")
b = []
if len(a) >= 2:
    for i in a:
        i = i.split("+")
        i = [int(x) for x in i]
        b.append(str(sum(i)))
else:
    b = a
print(eval("-".join(b)))
