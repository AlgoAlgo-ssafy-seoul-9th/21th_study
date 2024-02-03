import sys
input = sys.stdin.readline

dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def go_up(board):
    for i in range(M):
        nums = []
        cnt = -1
        for j in range(N):
            tmp = board[j][i]
            if tmp != 0:
                nums.append(tmp)
                cnt += 1
                board[j][i] = 0
        while cnt != -1:
            board[cnt][i] = nums.pop()
            cnt -= 1
    
    return board

def go_down(board):
    for i in range(M):
        nums = []
        cnt = -1
        for j in range(N):
            tmp = board[j][i]
            if tmp != 0:
                nums.append(tmp)
                cnt += 1
                board[j][i] = 0
        idx = 0
        while cnt != -1:
            board[N-1-idx][i] = nums.pop()
            cnt -= 1
            idx += 1
    return board

def bomb(board):
    visited = [[0]*M for _ in range(N)]
    check = []
    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                if board[i][j]:
                    visited[i][j] = 1
                    tmp = board[i][j]
                    tmp_checker = False
                    for d in dxy:
                        nx = i + d[0]
                        ny = j + d[1]

                        if 0 <= nx <= N-1 and 0 <= ny <= M-1:
                            visited[nx][ny] = 1
                            if board[nx][ny] == tmp:
                                check.append([nx, ny])
                                tmp_checker = True
                    if tmp_checker:
                        check.append([i, j])
    for v in check:
        board[v[0], v[1]] = 0
    
    return board




N, M, Q = map(int, input().split())

board = [[0]*M for _ in range(N)]

for _ in range(Q):
    order, *remain = map(int, input().split())
    if order == 1:
        x, y, num = remain[0], remain[1], remain[2]
        x -= 1
        y -= 1
        if board[x][y] == 0 or board[x][y] < num:
            board[x][y] = num
    elif order == 2:
        while True:
            board = go_up(board)
            board_check = [[board[i][j] for j in range(M)] for i in range(N)]
            board = bomb(board)
            if board_check == board:
                break
    elif order == 3:
        while True:
            board = go_down(board)
            board_check = [[board[i][j] for j in range(M)] for i in range(N)]
            board = bomb(board)
            if board_check == board:
                break
    else:
        x, y = remain[0], remain[1]
        x -= 1
        y -= 1
        board[x][y] = 0

for line in board:
    print(*line)