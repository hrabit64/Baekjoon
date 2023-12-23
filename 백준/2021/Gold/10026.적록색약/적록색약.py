import sys
from collections import deque
nx = [1,-1,0,0]
ny = [0,0,-1,1]
sys.setrecursionlimit(100000)
def dfs(dx,dy,target):

    if 0<=dx and dx < N and \
        0 <= dy and dy < N and \
        area[dy][dx] == target and \
            (dx,dy) not in visited:
        
        visited.add((dx,dy))

        for i in range(4):
            dfs(dx+nx[i],dy+ny[i],target)

    else:
        return

area = []
N = int(sys.stdin.readline().strip())

q_green = deque()
cnt_normal = 0
cnt_green = 0



for i in range(N):
    idx = sys.stdin.readline().strip()
    for j,color in enumerate(idx):
        if color == "G":
            q_green.append((j,i))
    area.append([i for i in idx])

visited = set()
for i in range(N):
    for j in range(N):
        if (j,i) not in visited:
            dfs(j,i,area[i][j])
            cnt_normal += 1

if q_green:
    for x,y in q_green:
        area[y][x] = "R"

visited = set()
for i in range(N):
    for j in range(N):
        if (j,i) not in visited:
            dfs(j,i,area[i][j])
            cnt_green += 1


sys.stdout.write(str(cnt_normal) + " " + str(cnt_green) + "\n")