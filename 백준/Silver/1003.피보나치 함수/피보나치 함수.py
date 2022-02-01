import sys
n = int(sys.stdin.readline().strip())
nums = [int(sys.stdin.readline().strip()) for _ in range(n)]

fibo_out_zero = [1,0,1,1]
fibo_out_one = [0,1,1,2]
for num in nums:

    if num <= len(fibo_out_zero)-1:
        sys.stdout.write(str(fibo_out_zero[num])+" "+str(fibo_out_one[num])+"\n")
    else:
        for i in range(len(fibo_out_zero),num+1):
            fibo_out_zero.append(fibo_out_zero[i-1]+fibo_out_zero[i-2])
            fibo_out_one.append(fibo_out_one[i - 1] + fibo_out_one[i - 2])
        sys.stdout.write(str(fibo_out_zero[num])+" "+str(fibo_out_one[num])+"\n")