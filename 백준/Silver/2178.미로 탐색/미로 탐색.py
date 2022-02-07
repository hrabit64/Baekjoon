import sys
from collections import deque

sys.setrecursionlimit(100000)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    q = deque()
    q.append((x,y))

    while q:
        x,y = q.popleft()

        for t in range(4):
            target_x = x + dx[t]
            target_y = y + dy[t]

            if target_x < 0 or target_x >= M or\
                target_y < 0 or target_y >= N:
                continue

            if m[target_y][target_x] == 0:
                continue

            if m[target_y][target_x] == 1:
                m[target_y][target_x] = m[y][x] + 1
                q.append((target_x,target_y))

    return m[N-1][M-1]



N,M = (map(int,sys.stdin.readline().strip().split()))

m = []

for _ in range(N):
    m.append([int(x) for x in sys.stdin.readline().strip()])

sys.stdout.write(str(bfs(0,0)))
