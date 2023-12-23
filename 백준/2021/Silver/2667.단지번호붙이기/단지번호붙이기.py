import sys
from collections import defaultdict
sys.setrecursionlimit(100000)

def dfs(ground, target_x, target_y,target):
    if target_x < 0 or target_x >= N or \
            target_y < 0 or target_y >= N or \
            ground[target_x][target_y] != 1:
        return

    ground[target_x][target_y] = -1
    house[target] += 1

    dfs(ground, target_x - 1, target_y,target)
    dfs(ground, target_x + 1, target_y,target)
    dfs(ground, target_x, target_y - 1,target)
    dfs(ground, target_x, target_y + 1,target)

N = int(sys.stdin.readline().strip())
m = []
cnt = 0
house = defaultdict(int)
for _ in range(N):

    m.append([int(x) for x in sys.stdin.readline().strip()])

for i in range(N):
    for j in range(N):
        if m[i][j] == 1:
            dfs(m,i,j,cnt+2)
            cnt += 1

sys.stdout.write(str(cnt)+"\n")
sys.stdout.write("\n".join(str(x) for x in sorted(list(house.values()))))