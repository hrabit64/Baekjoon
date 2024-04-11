import collections



moves = [(1,0),(-1,0),(0,1),(0,-1)]

maze_map = []

    

N,M = tuple(map(lambda x: int(x),input().split(" ")))
start = None

for i in range(N):
    line = []

    for j,x in enumerate(input()):

        if x == "0" :
            start = (j,i)
        line.append(x)
    maze_map.append(line)


def bfs(start) -> int:
    start_inventory = ["0" for _ in range(6)]
    queue = collections.deque([(start,start_inventory)])
    visited = set([(start,"".join(start_inventory))])
    move_cnt = collections.defaultdict(int)
    move_cnt[(start,"".join(start_inventory))] = 0
    


    while queue:
        position,inv = queue.popleft()
        x ,y = position
        prev_cnt = move_cnt[((x,y),"".join(inv))]
        for move in moves:
            dx = x + move[0]
            dy = y + move[1]
            inventory = inv[:]
            
            if ((dx,dy),"".join(inventory)) not in visited and dx >= 0 and dx < M and dy >= 0 and dy < N:

        
                if maze_map[dy][dx] == "#":
                    continue

                elif maze_map[dy][dx] in ['a', 'b', 'c', 'd', 'e', 'f'] and inventory[ord(maze_map[dy][dx].upper())-65] == "0":
                    inventory[ord(maze_map[dy][dx].upper())-65] = "1"


                elif maze_map[dy][dx] in ['A', 'B', 'C', 'D', 'E', 'F'] and inventory[ord(maze_map[dy][dx].upper())-65] == "0":
                    continue
                
                queue.append(((dx,dy),inventory))
                move_cnt[((dx,dy),"".join(inventory))] = prev_cnt + 1
                visited.add(((dx,dy),"".join(inventory)))
             

                if maze_map[dy][dx] == "1":
                    return move_cnt[((dx,dy),"".join(inventory))]

    return -1
        
print(bfs(start))