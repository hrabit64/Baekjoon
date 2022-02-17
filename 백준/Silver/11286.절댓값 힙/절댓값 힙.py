import sys
import heapq

def solve():
    heap = []
    N = int(sys.stdin.readline().strip())
    for _ in range(N):

        command = int(sys.stdin.readline().strip())

        if command == 0:
            if heap:
                x = heapq.heappop(heap)
                x = -1*x//10 if not x % 10 else x//10

                sys.stdout.write(str(x)+"\n")
            else:
                sys.stdout.write("0\n")

        else:

            num = abs(command)*10 if command < 0 else abs(command)*10+1
            heapq.heappush(heap,num)

solve()