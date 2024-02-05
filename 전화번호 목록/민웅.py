# 5052_전화번호목록_list of phone-numbers
# 10% 시간초과
import sys
input = sys.stdin.readline


def number_insert(wd, pn):
    now_dict = wd
    ans = True
    for number in pn:
        if number in now_dict.keys() and 'E' in now_dict[number].keys():
            return False
        if number not in now_dict.keys():
            now_dict[number] = {}
        now_dict = now_dict[number]

        if 'E' in now_dict:
            return False
    now_dict['E'] = True

    return ans


T = int(input())

for _ in range(T):
    word_dict = {}
    N = int(input())
    ans = True
    num_lst = []
    for i in range(N):
        PN = input().strip()
        num_lst.append(PN)
    num_lst.sort()
    for pn in num_lst:
        if not number_insert(word_dict, pn):
            ans = False
            break
    if ans:
        print("YES")
    else:
        print("NO")

