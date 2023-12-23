import sys

T = int(sys.stdin.readline().strip())
memo_l = [0,1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
memo = [0 for i in range(101)]

for i in range(len(memo_l)):
    memo[i] = memo_l[i]

def dp(n):
    ptr = 10
    while not memo[n]:
        memo[ptr] = memo[ptr-2] + memo[ptr-3]
        ptr += 1
    return memo[n]

for _ in range(T):

    N = int(sys.stdin.readline().strip())
    sys.stdout.write(str(dp(N))+"\n")

