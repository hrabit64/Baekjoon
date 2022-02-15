import sys
from collections import deque


def main():

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    sys.setrecursionlimit(100000)

    M, N = map(int, sys.stdin.readline().strip().split())
    q = deque([])
    boxes = []

    def bfs():
        while q:
            m,n = q.popleft()
            for i in range(len(dy)):
                nx = m+dx[i]
                ny = n+dy[i]

                if 0 <= nx and nx < M and \
                    0 <= ny and ny < N and \
                    boxes[ny][nx] == 0:
                    q.append((nx,ny))
                    boxes[ny][nx] = boxes[n][m] + 1

    cnt = 0
    for n in range(N):
        row = list(map(int,sys.stdin.readline().strip().split()))
        for m,num in enumerate(row):
            if num == 1:
                q.append((m,n))
            elif num == 0:
                cnt += 1

        boxes.append(row)

    if cnt == 0:
        sys.stdout.write("0\n")

    else:
        day_cnt = 0
        bfs()
        for n in boxes:
            if 0 in n:
                sys.stdout.write("-1\n")
                return

            day_cnt = max(day_cnt,max(n))

        sys.stdout.write(str(day_cnt-1)+"\n")

main()