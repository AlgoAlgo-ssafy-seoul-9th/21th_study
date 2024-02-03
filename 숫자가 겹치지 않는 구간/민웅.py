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