import sys
input = sys.stdin.readline

# 주어진 좌표가 범위 안에 있는지 확인
def isOutrange(x, y):
    if 0 <= x <= N-1 and 0 <= y <= M-1:
        return True

# 기울였을 때 위로 이동
def moveUp():
    for i in range(1, N):
        for j in range(M):
            tmp = i
            while tmp >= 1:
                if board[tmp][j] and not board[tmp-1][j]:   # 한 칸 위가 0이고 본인은 0이 아니면
                    board[tmp-1][j], board[tmp][j] = board[tmp][j], board[tmp-1][j]     # 둘이 바꿈
                tmp -= 1
    return board

# 기울였을 때 아래로 이동
def moveDown():
    for i in range(N-2, -1, -1):
        for j in range(M):
            tmp = i
            while tmp <= N-2:
                if board[tmp][j] and not board[tmp+1][j]:   # 한 칸 아래가 0이고 본인은 0이 아니면
                    board[tmp+1][j], board[tmp][j] = board[tmp][j], board[tmp+1][j]     # 둘이 바꿈
                tmp += 1
    return board

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 같은 번호 블럭 삭제
def deleteSame():
    isSame = [[0] * M for _ in range(N)]
    isChanged = False
    for i in range(N):
        for j in range(M):
            for d in range(4):
                if isOutrange(i + dx[d], j + dy[d]):
                        if board[i][j] != 0 and board[i][j] == board[i + dx[d]][j + dy[d]] and not isSame[i + dx[d]][j + dy[d]]:
                            board[i + dx[d]][j + dy[d]] = 0
                            isSame[i + dx[d]][j + dy[d]] = 1
                            isChanged = True
            if isChanged:
                isSame[i][j] = 1

N, M, Q = map(int, input().split())
board = [[0] * M for _ in range(N)]

for _ in range(Q):
    play = list(map(int, input().split()))
    if play[0] == 1:        # 첫번째 놀이
        if board[play[1]-1][play[2]-1] < play[3]:
            board[play[1]-1][play[2]-1] = play[3]
    elif play[0] == 2:      # 두번째 놀이
        moveUp()
        deleteSame()
    elif play[0] == 3:      # 세번째 놀이
        moveDown()
        deleteSame()
    elif play[0] == 4:     # 네번째 놀이
        board[play[1]-1][play[2]-1] = 0

for row in board:
    print(*row)