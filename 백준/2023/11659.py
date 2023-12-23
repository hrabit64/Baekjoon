# https://www.acmicpc.net/problem/11659

N, M = tuple(map(int, input().split(" ")))

nums = list(map(int, input().split(" ")))

prefix_sums = [nums[0]]

for x in range(1,N):
    prefix_sums.append(prefix_sums[-1]+nums[x])

res = []

for _ in range(M):
    i,j = tuple(map(int, input().split(" ")))
    
    if i - 1 <= 0:
        res.append(prefix_sums[j-1])
    else:
        res.append(prefix_sums[j-1] - prefix_sums[i-2])
        
for x in res:
    print(x)
    
# 오답노트

#부분 합 알고리즘 활용하기 ref : https://code-angie.tistory.com/22