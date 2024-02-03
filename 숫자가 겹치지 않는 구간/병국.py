from collections import deque

n = int(input())
num_list = list(map(int,input().split()))
answer = 0

stack = deque()

for i in range(n):
    if stack and num_list[i] in stack:
        while True:
            aa = stack[0]
            if aa == num_list[i]:
                stack.popleft()
                break
            stack.popleft()
    stack.append(num_list[i])
    answer = max(len(stack),answer)
    # print(answer,stack,len(stack))
print(answer)