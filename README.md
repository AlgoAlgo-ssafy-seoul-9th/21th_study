# 21th_study

# 이번주 스터디 문제
<details markdown="1" open>
<summary>접기/펼치기</summary>

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
```
### [성구](./숫자가%20겹치지%20않는%20구간/성구.py)
```py
```
### [승우](./숫자가%20겹치지%20않는%20구간/승우.py)
```py
```
</details>

# 알고리즘 설명
<details markdown="1">
<summary>접기/펼치기</summary>
</details>