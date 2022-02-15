import sys
from collections import defaultdict
import heapq

T = int(sys.stdin.readline().strip())



for _ in range(T):
    k = int(sys.stdin.readline().strip())
    stop = False
    low_heap = []
    high_heap = []
    hash_dic = defaultdict(int)

    for _ in range(k):
        command, num = sys.stdin.readline().strip().split()

        if command == 'I':
            heapq.heappush(low_heap, int(num))
            heapq.heappush(high_heap, -int(num))
            hash_dic[num] += 1

        if command == 'D':

            if num == '1':
                while len(high_heap) and not hash_dic[str(-high_heap[0])]:
                    _ = heapq.heappop(high_heap)

                if high_heap:
                    hash_dic[str(-heapq.heappop(high_heap))] -= 1

            elif num == '-1':
                while len(low_heap) and not hash_dic[str(low_heap[0])]:
                    _ = heapq.heappop(low_heap)

                if low_heap:
                    hash_dic[str(heapq.heappop(low_heap))] -= 1

    while len(low_heap) and not hash_dic[str(low_heap[0])]:
        _ = heapq.heappop(low_heap)

    while len(high_heap) and not hash_dic[str(-high_heap[0])]:
        _ = heapq.heappop(high_heap)

    if len(low_heap) > 0:
        sys.stdout.write(str(-heapq.heappop(high_heap))+" "+str(heapq.heappop(low_heap))+"\n")

    else:
        sys.stdout.write("EMPTY\n")
