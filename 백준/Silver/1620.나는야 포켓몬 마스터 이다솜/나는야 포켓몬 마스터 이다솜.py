import sys
import math

N,M = tuple(map(int,sys.stdin.readline().strip().split()))
dic = dict()

for i in range(N):

    target = sys.stdin.readline().strip()
    dic[str(i+1)] = target
    dic[target] = str(i+1)

for _ in range(M):
    q = sys.stdin.readline().strip()
    sys.stdout.write(str(dic[q])+"\n")