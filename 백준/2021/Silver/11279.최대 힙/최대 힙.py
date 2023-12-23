import sys
import heapq

def solve():
    heap = []
    N = int(sys.stdin.readline().strip())
    for _ in range(N):

        command = int(sys.stdin.readline().strip())

        if command == 0:
            if heap:
                sys.stdout.write(str(-heapq.heappop(heap))+"\n")
            else:
                sys.stdout.write("0\n")

        else:
            heapq.heappush(heap,-command)

solve()