def up():
    while True:        
        for i in range(m):
            num_arr = []
            for j in range(n):
                if arr[j][i] != 0:
                    num_arr.append(arr[j][i])
                    arr[j][i] = 0
            if len(num_arr) != 0:
                for k in range(len(num_arr)):
                    arr[k][i] = num_arr[k]
        # tmp = arr
        tmp = delete()
        # print(tmp)
        # print(tmp,'sadsadsa')
        if tmp == 0:
            break

def down():
    while True:   
        for i in range(m):
            num_arr = []
            for j in range(n):
                if arr[j][i] != 0:
                    num_arr.append(arr[j][i])
                    arr[j][i] = 0
            if len(num_arr) != 0:
                tmp2 = 0
                for k in range(n-len(num_arr),n):
                    arr[k][i] = num_arr[tmp2]
                    tmp2 += 1
        tmp = delete()
        # print(tmp,'sadsadsa')
        if tmp == 0:
            break



dir = [(1,0),(0,1),(-1,0),(0,-1)]
def delete():
    global v
    tmp = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                continue
            cnt = 0
            me = arr[i][j]
            v[i][j] = 1
            q = [(i,j)]
            while q:
                x,y = q.pop(0)
                for dx,dy in dir:
                    nx = x+dx
                    ny = y+dy
                    if 0<=nx<n and 0<=ny<m and v[nx][ny] == 0:
                        if me == arr[nx][ny]:
                            # print(me,arr[nx][ny],(nx,ny))
                        # 방문처리하고 0만들어주기
                            v[nx][ny] = 1
                            q.append((nx,ny))
                            arr[nx][ny] = 0
                            cnt += 1
                            tmp += 1
                # print(q)
            if cnt != 0:
                arr[i][j] = 0
    return tmp


n, m, q = map(int,input().split())

arr = [[0] * m for _ in range(n)]
v = [[0] * m for _ in range(n)]

for i in range(q):
    num,*play = list(map(int,input().split()))
    # print(num,play)
    if num == 1:
        if arr[play[0]-1][play[1]-1] != 0:
            arr[play[0]-1][play[1]-1] = max(arr[play[0]-1][play[1]-1],play[2])
        else:
            arr[play[0]-1][play[1]-1] = play[2]
    elif num == 4:
        arr[play[0]-1][play[1]-1] = 0
    elif num == 2:
        up()
    elif num == 3:
        down()
    # print(arr)
for i in range(n):
    print(*arr[i])