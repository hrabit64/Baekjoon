import sys
import math

def isCan(num):
    for i in str(num):

        if int(i) not in buttons:

            return False

    return True


N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())


broken_buttons = []

if M:
    broken_buttons = list(map(int, sys.stdin.readline().strip().split()))

buttons = [x for x in range(10) if x not in broken_buttons]

if len(buttons):

    min_abs, cnt_near = math.inf, 0
    for num in range(1000000):

        if isCan(num):

            if min_abs > abs(N-num):

                min_abs = abs(N-num)

                cnt_near = int(math.log10(num))+1 if not num == 0 else 1

            if not min_abs:
                break

    cnt_plus_one = abs(N-100)
    cnt_near += min_abs
    cnt = min(cnt_plus_one,cnt_near)

    sys.stdout.write(str(cnt))


else:
    sys.stdout.write(str(abs(N-100)))