import sys
import math
from collections import deque,defaultdict


class BFS:

    def __init__(self,graph):
        self.graph = graph

    def run(self,start_node):
        visited = [str(start_node)]
        q = deque()
        q.append(start_node)
        bacons = [0 for i in range(N+1)]
        while q:
            node = q.popleft()

            for w in self.graph[node]:
                if w not in visited:
                    visited.append(w)
                    q.append(w)
                    bacons[w] += bacons[node]+1

        return bacons

N,M = tuple(map(int,sys.stdin.readline().strip().split()))

graph = defaultdict(list)

for _ in range(M):
    a, b = tuple(map(int, sys.stdin.readline().strip().split()))
    graph[a].append(b)
    graph[b].append(a)

bfs = BFS(graph)

min_bacon,min_person = math.inf,None

for i in range(N):

    cnt = sum(bfs.run(i+1))

    if min_bacon > cnt:
        min_bacon,min_person = cnt,i+1


sys.stdout.write(str(min_person))
