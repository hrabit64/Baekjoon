import sys
import heapq

q = []
N = int(sys.stdin.readline().strip())
for _ in range(N):
    command = int(sys.stdin.readline().strip())
    if not command:
        if not len(q):
            sys.stdout.write("0\n")
        else:
            sys.stdout.write(str(heapq.heappop(q)))
            sys.stdout.write("\n")

    else:
        heapq.heappush(q,command)
