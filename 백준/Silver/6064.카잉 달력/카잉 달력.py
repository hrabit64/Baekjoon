import sys

def check():
    global x,y
    if x == M:
        x = 0
    if y == N:
        y = 0
    for i in range(x,M*N,M):
        if i % N == y:
            return i

    return False

T = int(sys.stdin.readline().strip())

for _ in range(T):
    M,N,x,y = map(int,sys.stdin.readline().strip().split())
    t = check()
    if t:
        print(t)
    else:
        print("-1")






