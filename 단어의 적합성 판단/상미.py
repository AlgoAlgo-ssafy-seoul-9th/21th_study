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

    for i in range(len(word)-1):
        if word[i] == word[i+1] and word[i] not in ['e', 'o']:
            break
    else:
        cond3 = True
    
    if cond1 and cond2 and cond3:
        print(1)
    else:
        print(0)