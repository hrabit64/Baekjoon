import sys
from collections import deque

def main():
    N,K = map(int,sys.stdin.readline().strip().split())

    values = []

    for _ in range(N):
        value = int(sys.stdin.readline().strip())
        if value == K:
            sys.stdout.write("1\n")
            return
        elif value <= K:
            values.append(value)
    max_ptr = len(values)-1
    target = 0
    cnt = 0
    while target != K and max_ptr >= 0:
        while target+values[max_ptr] <= K:
            target += values[max_ptr]
            cnt += 1


        max_ptr -= 1

    sys.stdout.write(str(cnt) + "\n")

main()