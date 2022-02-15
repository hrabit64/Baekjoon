import sys
from collections import deque

def bfs():
    before,after = map(int,sys.stdin.readline().strip().split())
    q = deque([(before,"")])
    nums = [False for _ in range(10001)]
    while q:
        target_num,path = q.popleft()

        n_nums = []

        #D
        d_num = target_num*2
        if d_num > 9999:
            d_num = d_num % 10000
        n_nums.append(d_num)

        #S
        s_num = target_num - 1
        if s_num == -1:
            s_num = 9999
        n_nums.append(s_num)

        #L
        l_num = target_num % 1000 * 10 + target_num // 1000
        n_nums.append(l_num)

        #R
        r_num = target_num % 10 * 1000 + target_num // 10
        n_nums.append(r_num)

        for idx,n_num in enumerate(n_nums):
            if 0 <= n_num and n_num <= 9999 and not nums[n_num]:

                if n_num == after:
                    return path+dslr[idx]

                else:
                    q.append((n_num,path+dslr[idx]))
                    nums[n_num] = True

T = int(sys.stdin.readline().strip())
dslr = ['D','S','L','R']

for _ in range(T):
    fin_path = bfs()
    sys.stdout.write(fin_path+"\n")