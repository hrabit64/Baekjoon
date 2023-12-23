# https://www.acmicpc.net/problem/11399

N = input()
P = sorted(list(map(int, input().split(" "))))
sum_t = P[0]

for i in range(1, len(P)):
    sum_t += sum(P[0:i+1])
    
print(sum_t)
