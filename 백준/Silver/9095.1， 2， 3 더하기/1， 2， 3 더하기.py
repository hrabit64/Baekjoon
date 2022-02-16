import sys
from collections import deque

def bfs():
    target = int(sys.stdin.readline().strip())
    q = deque([(0,0)])
    path_list = []
    while q:
        q_num,path = q.popleft()

        for i in range(3):
            n_num = q_num + i + 1
            if 0 <= n_num and n_num < 11:

                if n_num == target:
                    path_list.append(path+1)

                else:
                    q.append((n_num,path+1))

    return path_list
T = int(sys.stdin.readline().strip())

for _ in range(T):
    path_list = bfs()
    sys.stdout.write(str(len(path_list))+"\n")