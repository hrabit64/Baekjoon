import sys

def check_same(array):
    target = array[0][0]

    for i in range(len(array)):
        for j in range(len(array)):
            if not target == array[i][j]:
                return False

    return True

def loop(array):
    if not check_same(array):

        loop([row[0:len(array)//2] for row in array[0:len(array)//2]])
        loop([row[0:len(array)//2] for row in array[len(array)//2:len(array)]])
        loop([row[len(array)//2:len(array)] for row in array[0:len(array)//2]])
        loop([row[len(array)//2:len(array)] for row in array[len(array)//2:len(array)]])

    else:
        cnt[array[0][0]] += 1

N = int(sys.stdin.readline().strip())
paper = []
cnt = [0,0]
for _ in range(N):

    paper.append(list(map(int,sys.stdin.readline().strip().split())))

loop(array=paper)
sys.stdout.write("\n".join(str(x) for x in cnt))


