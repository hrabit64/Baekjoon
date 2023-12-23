import sys
from collections import deque


N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())
s = sys.stdin.readline().strip()

ptr = 0
cnt = 0

while ptr < M:

    if s[ptr] == 'I':

        sub_ptr = ptr + 1
        streak = 0

        while sub_ptr+2 < M:
            if s[sub_ptr:sub_ptr+2] == "OI":
                streak += 1
            else:
                break

            sub_ptr += 2
        if streak > N-1:
            cnt += streak-(N-1)
        ptr = sub_ptr - 1
    ptr += 1

print(cnt)


