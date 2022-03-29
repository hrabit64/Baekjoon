from collections import deque

def main():
    n = int(input())

    input_array = []
    output_array = ["+"]

    nums = [i for i in range(2,n+1)]

    stack = deque()
    stack.append(1)
    for _ in range(n):
        input_array.append(int(input()))

    pointer = 0

    while pointer < n:

        if len(stack) == 0:
            stack.append(nums[0])
            nums.remove(nums[0])
            output_array.append("+")

        if input_array[pointer] < stack[-1]:
            print("NO",end="")
            return None

        while input_array[pointer] != stack[-1]:
            stack.append(nums[0])
            nums.remove(nums[0])
            output_array.append("+")

        output_array.append("-")
        stack.pop()
        pointer += 1


    for i in output_array:
        print(i)


main()