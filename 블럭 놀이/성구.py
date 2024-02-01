import sys
input = sys.stdin.readline

N, M, Q = map(int, input().split())
board = [[0] * M for _ in range(N)]
near = [(0,1), (0,-1),(1,0),(-1,0)]

def putin(i:int, j:int, num:int):
    board[i-1][j-1] = max(board[i-1][j-1], num)


def up():
    candi = 0
    for j in range(M):
        nums = []
        for k in range(N):
            if board[k][j]:
                nums.append(board[k][j])
                board[k][j] = 0
        if nums:
            for k in range(len(nums)):
                board[k][j] = nums[k]
        
    for j in range(M):
        for di, dj in near:
            ni, nj = di, j+dj
            if 0<=ni<N and 0<= nj <M and board[0][j] != 0 and board[0][j] == board[ni][nj]:
                board[0][j] = 0
                board[ni][nj] = 0
                candi += 1
    if candi:
        return 1
    
    return 0

def down():
    candi = 0
    for j in range(M):
        nums = []
        for k in range(N-1,-1,-1):
            if board[k][j]:
                nums.append(board[k][j])
                board[k][j] = 0
        if nums:
            for k in range(len(nums)):
                board[N-1-k][j] = nums[k]
        
    for j in range(M):
        for di, dj in near:
            ni, nj = N-1+di, j+dj
            if 0<=ni<N and 0<= nj <M and board[N-1][j] != 0 and board[N-1][j] == board[ni][nj]:
                board[0][j] = 0
                board[ni][nj] = 0
                candi += 1
    if candi:
        return 1
    
    return 0

def delete(i:int, j:int):
    board[i-1][j-1] = 0


for _ in range(Q):
    order, *actions = map(int, input().strip().split())
    if order == 1:
        putin(*actions)
    elif order == 2:
        while up():
            pass
    elif order == 3:
        while down():
            pass
    else:
        delete(*actions)
    
[print(*board[i]) for i in range(N)]