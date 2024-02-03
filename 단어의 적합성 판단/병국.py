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