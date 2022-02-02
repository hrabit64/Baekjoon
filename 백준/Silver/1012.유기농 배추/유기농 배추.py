import sys

sys.setrecursionlimit(100000)


def dfs(ground, target_x, target_y):
    if target_x < 0 or target_x >= m or \
            target_y < 0 or target_y >= n or \
            ground[target_x][target_y] != 1:
        return

    ground[target_x][target_y] = 0

    dfs(ground, target_x - 1, target_y)
    dfs(ground, target_x + 1, target_y)
    dfs(ground, target_x, target_y - 1)
    dfs(ground, target_x, target_y + 1)


T = int(sys.stdin.readline().strip())

for _ in range(T):

    m, n, k = tuple(map(int, sys.stdin.readline().strip().split()))
    ground = [[0] * n for _ in range(m)]
    count = 0
    for _ in range(k):
        x, y = tuple(map(int, sys.stdin.readline().strip().split()))
        ground[x][y] = 1

    for x in range(m):
        for y in range(n):
            if ground[x][y] == 1:
                dfs(ground, x, y)
                count += 1

    sys.stdout.write(str(count) + "\n")
