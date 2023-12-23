import sys
from collections import deque


def main():
    dh = [1,-1,0,0,0,0]
    dx = [0,0,-1,1,0,0]
    dy = [0,0,0,0,-1,1]
    sys.setrecursionlimit(100000)

    M, N, H = map(int, sys.stdin.readline().strip().split())
    q = deque([])
    boxes = []

    def bfs():
        while q:
            m,n,h = q.popleft()
            for i in range(len(dh)):
                nx = m+dx[i]
                ny = n+dy[i]
                nh = h+dh[i]

                if 0 <= nx and nx < M and \
                    0 <= ny and ny < N and \
                    0 <= nh and nh < H and \
                    boxes[nh][ny][nx] == 0:
                    q.append((nx,ny,nh))
                    boxes[nh][ny][nx] = boxes[h][n][m] + 1


    cnt = 0
    for h in range(H):
        one_stack = []
        for n in range(N):
            row = list(map(int,sys.stdin.readline().strip().split()))
            for m,num in enumerate(row):
                if num == 1:
                    q.append((m,n,h))
                elif num == 0:
                    cnt += 1
            one_stack.append(row)
        boxes.append(one_stack)

    if cnt == 0:
        sys.stdout.write("0\n")

    else:
        day_cnt = 0
        bfs()
        for h in boxes:
            for n in h:
                if 0 in n:
                    sys.stdout.write("-1\n")
                    return

                day_cnt = max(day_cnt,max(n))

        sys.stdout.write(str(day_cnt-1)+"\n")


main()