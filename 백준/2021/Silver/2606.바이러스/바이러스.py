import sys
from collections import defaultdict

def dfs(start_node,graph):
    stack = [start_node]
    infection = set()
    while stack:
        node = stack.pop()

        if node not in infection:
            infection.add(node)
            for w in graph[node]:
                stack.append(w)

    return infection
_ = int(sys.stdin.readline().strip())
N = int(sys.stdin.readline().strip())
graph = defaultdict(list)


for _ in range(N):
    a,b = map(int,sys.stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)

sys.stdout.write(str(len(dfs(1,graph))-1))