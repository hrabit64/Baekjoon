import sys
import math
N = int(sys.stdin.readline().strip())
rooms = []
cnt = 0
for _ in range(N):
    nums = tuple(map(int,sys.stdin.readline().strip().split()))
    rooms.append((nums[0],nums[1]))

rooms.sort(key=lambda x: (x[1],x[0]))

prev_end = 0
for start,end in rooms:

    if start >= prev_end:
        cnt += 1
        prev_end = end

sys.stdout.write(str(cnt))