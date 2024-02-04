# 21th_study

<br/>

# 이번주 스터디 문제

<details markdown="1" open>
<summary>접기/펼치기</summary>

<br/>

## [전화번호 목록](https://www.acmicpc.net/problem/5052)

### [민웅](./전화번호%20목록/민웅.py)

```py

```

### [병국](./전화번호%20목록/병국.py)

```py
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    phone_list = []
    for i in range(n):
        num = input().rstrip()
        phone_list.append(num)
    flag = 'YES'
    phone_list.sort()
    # print(phone_list)
    for i in range(n-1):
        check = phone_list[i]
        len_check = len(check)
        tmp = phone_list[i+1]
        len_tmp = len(tmp)
        if len_check < len_tmp:
            if check == tmp[:len_check]:
                flag = 'NO'
    print(flag)

```

### [상미](./전화번호%20목록/상미.py)

```py

```

### [성구](./전화번호%20목록/성구.py)

```py
# 5052 전화번호 목록
import sys
input = sys.stdin.readline

# Trie에 사용할 Node
class Node:
    def __init__(self, key:int,data=False) -> None:
        self.key = key
        self.data = data
        self.children = {}

# Trie 알고리즘
class Trie:
    # 클래스 생성 시 생성자
    def __init__(self) -> None:
        # 가장 최상위 루트, 시작점
        self.root = Node(None)

    # 단어를 Trie 에 넣으면서 체크
    def insert(self, string:str) -> bool:
        # root에서 시작
        current_node = self.root
        for char in string:
            # 한글자씩 넣어보자
            # 다음 노드가 없으면
            if char not in current_node.children.keys():
                # 다음 노드에 현재를 넣음
                current_node.children[char] = Node(char)
            # 다음단계로 이동(현재 넣었던 노드를 키로 받아 사용)
            # children {char : Node<class>}
            current_node = current_node.children[char]
            if current_node.data:
                return True
        # 마지막에 끝남 처리
        current_node.data = True
        return False


def solution():
    number_book = Trie()
    N = int(input())
    # Trie 알고리즘은 탐색 알고리즘이기에 정렬이 필수
    numbers = sorted([input().strip() for _ in range(N)])
    flag = 0
    # 입력을 모두 받아야 다음 케이스가 정상적으로 돌아감
    for i in range(N):
        if flag:
            continue
        if number_book.insert(numbers[i]):
            print("NO")
            # 불필요한 탐색을 줄이기 위한 flag
            flag = 1

    else:
        if not flag:
            print("YES")
    return


if __name__ == "__main__":
    for _ in range(int(input())):
        solution()
```

### [승우](./전화번호%20목록/승우.py)

```py
import sys
input = sys.stdin.readline

def check(phonebook):
    for i in range(len(phonebook) - 1):
        if phonebook[i] == phonebook[i+1][:len(phonebook[i])]:
            return False
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    phonebook = [input().rstrip() for _ in range(n)]
    phonebook.sort()

    if check(phonebook):
        print('YES')
    else:
        print('NO')

```

</details>

<br/><br/>

# 지난주 스터디 문제

<details markdown="1">
<summary>접기/펼치기</summary>

## [단어의 적합성 판단](https://www.codetree.ai/problems/judgment-of-adequacy-of-words/description)

### [민웅](./단어의%20적합성%20판단/민웅.py)

```py
import sys
input = sys.stdin.readline

vowels = ['a', 'e', 'i', 'o', 'u']
exc = ['e', 'o']

N = int(input())



for _ in range(N):
    word = list(input().strip())
    l = len(word)

    is_vowel = False
    before_word = word[0]
    in_vowel = False

    sequential = 1

    ans = True

    if word[0] in vowels:
        is_vowel = True
        in_vowel = True
    if l > 1:
        for i in range(1, l):
            tmp = word[i]
            if tmp in vowels:
                in_vowel = True
                if is_vowel:
                    sequential += 1
                else:
                    is_vowel = True
                    sequential = 1
            else:
                if is_vowel:
                    is_vowel = False
                    sequential = 1
                else:
                    sequential += 1
            if tmp == before_word:
                if tmp not in exc:
                    ans = False
                    break
            before_word = tmp

            if sequential >= 3:
                ans = False
                break

    if not in_vowel:
        ans = False

    if ans:
        print(1)
    else:
        print(0)
```

### [병국](./단어의%20적합성%20판단/병국.py)

```py
mo_list = ['a','e','i','o','u']

n = int(input())
for _ in range(n):
    mo_cnt = 0
    mo = 0
    ja = 0
    arr = list(input())
    last = ''
    flag = True
    for i in range(len(arr)):
        if last != 'e' and last != 'o':
            if last == arr[i]:
                flag = False
        if arr[i] in mo_list:
            mo_cnt += 1
            mo += 1
            ja = 0
            if mo == 3:
                flag = False
        elif arr[i] not in mo_list:
            ja += 1
            mo = 0
            if ja == 3:
                flag = False
        last = arr[i]
        # print(mo,ja,flag)
    if flag == False or mo_cnt == 0:
        print(0)
    else:
        print(1)
```

### [상미](./단어의%20적합성%20판단/상미.py)

```py
import sys
input = sys.stdin.readline

n = int(input())
moeum = ['a', 'e', 'i', 'o', 'u']
for _ in range(n):
    word = input().strip()
    cond1, cond2, cond3 = False, False, False
    for w in word:
        if w in moeum:      # 첫번째 조건
            cond1 = True
            break
    cnt_m = 0
    cnt_j = 0
    for w in word:
        if w in moeum:
            cnt_m += 1
            cnt_j = 0
        else:
            cnt_j += 1
            cnt_m = 0
        if cnt_m == 3 or cnt_j == 3:    # 두번째 조건
            break
    else:
        cond2 = True

    for i in range(len(word)-1):        # 세번째 조건
        if word[i] == word[i+1] and word[i] not in ['e', 'o']:
            break
    else:
        cond3 = True

    if cond1 and cond2 and cond3:
        print(1)
    else:
        print(0)
```

### [성구](./단어의%20적합성%20판단/성구.py)

```py
import sys
input = sys.stdin.readline


def solution():
    n = int(input())
    moum = set(["a", "e", "i", "o", "u"])
    for _ in range(n):
        s = input().strip()
        # 모음, 자음개수, 모음개수, 같은 글자, e개수, o개수
        cnt = [0, 0, 0, 0, 0, 0, 0]
        for i in range(len(s)):
            if i == 0:
                if s[i] in moum:
                    cnt[0] = 1
                    cnt[2] += 1
                    if s[i] == "e":
                        cnt[4] += 1
                    elif s[i] == "o":
                        cnt[5] += 1
                    else:
                        cnt[3] +=1
                else:
                    cnt[1] =+ 1
                    cnt[3] +=1
                continue

            if s[i] in moum:
                cnt[0] =1
                cnt[2] += 1
                if s[i] == "e":
                    cnt[4] += 1
                    cnt[5] = 0
                    cnt[3] = 0
                elif s[i] == "o":
                    cnt[5] += 1
                    cnt[4] = 0
                    cnt[3] = 0
                else:
                    if s[i] == s[i-1] and s[i-1] in moum:
                        cnt[3] += 1
                    else:
                        cnt[3] = 1
                    cnt[4] = 0
                    cnt[5] = 0
                cnt[1] = 0
            else:
                if s[i] == s[i-1] and s[i-1] not in moum:
                    cnt[3] += 1
                else:
                    cnt[3] = 1
                cnt[1] += 1
                cnt[2] = 0
                cnt[4] = 0
                cnt[5] = 0
            if cnt[1] >=3 or cnt[2] >= 3 or cnt[4] >=3 or cnt[5]>=3 or cnt[3] >=2:
                print(0)
                break
        else:
            if cnt[0]:
                print(1)
            else:
                print(0)



if __name__ == "__main__":
    solution()
```

### [승우](./단어의%20적합성%20판단/승우.py)

```py

```

## [블럭 놀이](https://www.codetree.ai/problems/block-game/description)

### [민웅](./블럭%20놀이/민웅.py)

```py
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
```

### [병국](./블럭%20놀이/병국.py)

```py
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
```

### [상미](./블럭%20놀이/상미.py)

```py
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
```

### [성구](./블럭%20놀이/성구.py)

```py
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
```

### [승우](./블럭%20놀이/승우.py)

```py

```

## [숫자가 겹치지 않는 구간](https://www.codetree.ai/problems/non-overlapping-interval-of-nums/description)

### [민웅](./숫자가%20겹치지%20않는%20구간/민웅.py)

```py
import sys
input = sys.stdin.readline

N = int(input())

lst = list(map(int, input().split()))
num_dict = {}
i, j = 0, 0
ans = 0
while j < N:
    tmp = lst[j]
    if tmp not in num_dict.keys():
        num_dict[tmp] = 1
    else:
        if num_dict[tmp] == 1:
            while i < j:
                if lst[i] == tmp:
                    i += 1
                    break
                else:
                    num_dict[lst[i]] -= 1
                    i += 1
        else:
            num_dict[tmp] += 1
    if (j - i + 1) > ans:
        ans = (j - i + 1)
    j += 1
print(ans)
```

### [병국](./숫자가%20겹치지%20않는%20구간/병국.py)

```py
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
```

### [상미](./숫자가%20겹치지%20않는%20구간/상미.py)

```py
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

left, right = 0, 0
max_len = 0
num_set = set()
# nums[right] in nums[left:right]를 사용하여 중복을 확인하면 시간 복잡도가 O(N)이므로
# 입력이 100,000개의 숫자로 이루어져 있을 때 시간 초과

# 중복을 효율적으로 확인하기 위해 집합(Set) 사용
# Set은 중복된 값을 허용하지 않으며, 검색 연산(contains)의 시간 복잡도가 O(1)이기 때문에 더 효율적

while right < N:
    # 들어오는 수가 구간에 없으면
    if nums[right] not in num_set:
        num_set.add(nums[right])
        right += 1
        max_len = max(max_len, right - left)
    # 들어오는 수가 구간에 있으면
    else:
        num_set.remove(nums[left])
        left += 1

print(max_len)

```

### [성구](./숫자가%20겹치지%20않는%20구간/성구.py)

```py
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
```

### [승우](./숫자가%20겹치지%20않는%20구간/승우.py)

```py

```

</details>

<br/><br/>

# 알고리즘 설명

<details markdown="1">
<summary>접기/펼치기</summary>

<a href="https://l1m3kun.tistory.com/entry/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%AC%B8%EC%9E%90%EC%97%B4-%ED%8A%B8%EB%9D%BC%EC%9D%B4Trie">바로가기</a>

</details>
