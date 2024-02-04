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

