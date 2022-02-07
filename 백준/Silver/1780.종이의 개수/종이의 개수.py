import sys
def check(i,j,lenght,target,array):
    for e in range(i, i + lenght // 3):
        for f in range(j, j + lenght // 3):
            if not target == array[e][f]:
                loop(lenght // 3, [array[x][j:j + lenght // 3] for x in range(i, i + lenght // 3)])
                return False
    return True

def check_same(array,target):
    for i in range(N):
        for j in range(N):
            if not array[i][j] == target:
                return False
    return True

def loop(lenght,array):
    for i in range(0,lenght,lenght//3):

        for j in range(0, lenght, lenght // 3):
            target = array[i][j]
            x = check(i,j,lenght,target,array)
            if x:
                cnt[target+1] += 1


N = int(sys.stdin.readline().strip())
ground = []

for _ in range(N):
    ground.append(list(map(int,sys.stdin.readline().strip().split())))

cnt = [0,0,0]
c = True
for k in range(3):
    if check_same(ground,k-1):
        cnt[k] += 1
        sys.stdout.write("\n".join([str(x) for x in cnt]))
        c = False
        break
if c:
    loop(N,ground)
    sys.stdout.write("\n".join([str(x) for x in cnt]))