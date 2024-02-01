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