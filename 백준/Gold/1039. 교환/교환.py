from collections import deque


def bfs(N,K):
    visited = [(0,N)]
    queue = deque([(0,N)])
    test = [0,0,0]
    fin = []
    while queue:
        q = queue.popleft()

        if q[0] >= K:
            continue

        for i in range(len(N)-1):
            for j in range(i+1,len(N)):

                idx_N = q[1][:i] + q[1][j] + q[1][i+1:j] + q[1][i] + q[1][j+1:]

                if idx_N[0] == "0":
                    continue

                if (q[0]+1,idx_N) not in visited:

                    visited.append((q[0]+1,idx_N))
                    queue.append((q[0]+1,idx_N))

                    if(q[0]+1 == K):
                        fin.append(idx_N)

    if len(fin) == 0:
        return -1

    max_n = max(fin,key=lambda i:int(i))

    return max_n

def main():
    N,K = map(int,input().split(" "))
    if N < 10 and K != 0:
        return -1
    return bfs(str(N),K)
print(main())
