import sys

sys.setrecursionlimit(20)

N,r,c = tuple(map(int, sys.stdin.readline().strip().split()))
r,c = r+1,c+1

def get_z(N):
    cnt = 0

    if r == 1 and c == 1:
        return 0

    def loop(cnt,x,y):
        global r,c

        if x <= 1 and y <= 1:
            return cnt

        if x//2 >= c and y//2 >= r:
            return loop(cnt,x//2,y//2)

        elif x//2 * 2 >= c and y//2 >= r:

            cnt += x*y//4
            c = c - x//2
            return loop(cnt,x//2,y//2)

        elif x//2 >= c and y //2 * 2 >= r:
            cnt += x*y//4*2
            r = r - y//2
            return loop(cnt,x//2,y//2)

        else:
            cnt += x*y//4*3
            c,r = c - x//2,r - y//2
            return loop(cnt,x//2,y//2)

    return loop(cnt,2**N,2**N)

sys.stdout.write(str(get_z(N)))

