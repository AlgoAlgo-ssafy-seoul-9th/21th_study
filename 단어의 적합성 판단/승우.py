import sys
input = sys.stdin.readline

n = int(input())

vowels = ["a", "e", "i", "o", "u"]

def check_vowel(word):
    check = False
    for vowel in vowels:
        if vowel in word:
            check = True
    return check

for _ in range(n):
    word = input().rstrip()
    stack = [word[0], 1, word[0] in vowels]
    check = True
    if not check_vowel(word):
        print(0)
        continue


    for i in range(1, len(word)):
        cur_word = word[i]
        if cur_word == "e" and stack[0] == cur_word:
            stack[1] += 1
            continue
        elif cur_word == "o" and stack[0] == cur_word:
            stack[1] += 1
            continue
        elif stack[0] == cur_word:
            check = False
            break
        vowel_check = cur_word in vowels
        if vowel_check == stack[2]:
            stack[0] = cur_word
            stack[1] += 1
        else:
            stack[0] = cur_word
            stack[1] = 1
            stack[2] = vowel_check
        if stack[1] == 3:
            check = False
            break

    if check:
        print(1)
    else:
        print(0)