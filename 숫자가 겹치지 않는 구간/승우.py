import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
check = set()
queue = deque()
answer = 0

for i in range(N):

    if queue:
        answer = max(answer, len(queue))
        while queue and numbers[i] in check:
            check.discard(queue.popleft())
    queue.append(numbers[i])
    check.add(numbers[i])

print(answer)
