import sys
from collections import deque
input = sys.stdin.readline

def solution():
    N = int(input())
    arr = list(map(int, input().split()))
    visited = set()
    stack = deque([])
    maxlen = -1
    for i in range(N):
        if stack:
            maxlen = max(maxlen, len(stack))
            while stack and arr[i] in visited:
                s = stack.popleft()
                visited.discard(s)
        stack.append(arr[i])
        visited.add(arr[i])
    print(maxlen)

if __name__ == "__main__":
    solution()