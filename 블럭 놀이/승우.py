import sys
from collections import deque
input = sys.stdin.readline


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M, Q = map(int, input().split())
board = [[0 for _ in range(M)] for _ in range(N)]


def delete_block():
    delete_list = set()
    for i in range(N):
        for j in range(M):
            cur_block = board[i][j]
            if cur_block == 0:
                continue
            else:
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if (nx >= 0 and nx < N) and (ny >= 0 and ny < M) and cur_block == board[nx][ny]:
                        delete_list.add((i, j))

    if delete_list:
        for block in delete_list:
            board[block[0]][block[1]] = 0
        return False
    else:
        return True
    



def game_two():
    check = False
    while not check:
        for i in range(M):
            stack = deque()
            for j in range(N):
                if board[j][i]:
                    stack.append(board[j][i])
                    board[j][i] = 0
            idx = 0
            while stack:
                board[idx][i] = stack.popleft()
                idx += 1
                
        check = delete_block()

def game_three():
    check = False
    while not check:
        for i in range(M):
            stack = list()
            for j in range(N):
                if board[j][i]:
                    stack.append(board[j][i])
                    board[j][i] = 0
            idx = N - 1
            while stack:
                board[idx][i] = stack.pop()
                idx -= 1
                
        check = delete_block()


for _ in range(Q):
    game = list(map(int, input().split()))
    
    if game[0] == 1:
        board[game[1] - 1][game[2] - 1] = max(game[3],board[game[1] - 1][game[2] - 1])
    elif game[0] == 4:
        board[game[1] - 1][game[2] - 1] = 0
    elif game[0] == 2:
        game_two()
    else:
        game_three()


for line in board:
    print(*line)