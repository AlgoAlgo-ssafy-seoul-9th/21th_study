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
