import sys
n = int(sys.stdin.readline().strip())
nums = [int(sys.stdin.readline().strip()) for _ in range(n)]

fibo_out = [(1,0),(0,1),(1,1),(1,2)]
for num in nums:

    if num <= len(fibo_out)-1:
        sys.stdout.write(str(fibo_out[num][0])+" "+str(fibo_out[num][1])+"\n")
    else:
        for i in range(len(fibo_out),num+1):
            fibo_out.append((fibo_out[i-1][0]+fibo_out[i-2][0],fibo_out[i-1][1]+fibo_out[i-2][1]))
        sys.stdout.write(str(fibo_out[num][0])+" "+str(fibo_out[num][1])+"\n")



