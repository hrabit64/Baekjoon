import sys
def check(i,j,lenght,target,array):

    for e in range(i, i + lenght // 2):
        for f in range(j, j + lenght // 2):
            if not target == array[e][f]:
                sys.stdout.write("(")
                loop(lenght // 2, [array[x][j:j + lenght // 2] for x in range(i, i + lenght // 2)])
                return False
    return True

def check_same(array,target):
    for i in range(N):
        for j in range(N):
            if not array[i][j] == target:
                return False
    return True

def loop(lenght,array):
    for i in [0,lenght//2]:

        for j in [0,lenght//2]:

            target = array[i][j]
            x = check(i,j,lenght,target,array)

            if x:
                sys.stdout.write(str(target))

    sys.stdout.write(")")
N = int(sys.stdin.readline().strip())
img = []

for _ in range(N):
    img.append([int(x) for x in sys.stdin.readline().strip()])

if check_same(img,img[0][0]):
    sys.stdout.write(str(img[0][0]))

else:
    sys.stdout.write("(")
    loop(N,img)