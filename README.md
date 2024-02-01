# 21th_study

<br/>

# 이번주 스터디 문제

<details markdown="1" open>
<summary>접기/펼치기</summary>

<br/>

## [전화번호 목룍](https://www.acmicpc.net/problem/5052)

### [민웅](./전화번호%20목록/민웅.py)

```py

```

### [병국](./전화번호%20목록/병국.py)

```py

```

### [상미](./전화번호%20목록/상미.py)

```py

```

### [성구](./전화번호%20목록/성구.py)

```py

```

### [승우](./전화번호%20목록/승우.py)

```py

```

</details>

<br/><br/>

# 지난주 스터디 문제

<details markdown="1">
<summary>접기/펼치기</summary>

## [단어의 적합성 판단](https://www.codetree.ai/problems/judgment-of-adequacy-of-words/description)

### [민웅](./단어의%20적합성%20판단/민웅.py)

```py

```

### [병국](./단어의%20적합성%20판단/병국.py)

```py

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

```

### [병국](./블럭%20놀이/병국.py)

```py

```

### [상미](./블럭%20놀이/상미.py)

```py

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

```

### [병국](./숫자가%20겹치지%20않는%20구간/병국.py)

```py

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
</details>
