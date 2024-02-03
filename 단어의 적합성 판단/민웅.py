import sys
input = sys.stdin.readline

vowels = ['a', 'e', 'i', 'o', 'u']
exc = ['e', 'o']

N = int(input())



for _ in range(N):
    word = list(input().strip())
    l = len(word)

    is_vowel = False
    before_word = word[0]
    in_vowel = False
    
    sequential = 1

    ans = True

    if word[0] in vowels:
        is_vowel = True
        in_vowel = True
    if l > 1:
        for i in range(1, l):
            tmp = word[i]
            if tmp in vowels:
                in_vowel = True
                if is_vowel:
                    sequential += 1
                else:
                    is_vowel = True
                    sequential = 1
            else:
                if is_vowel:
                    is_vowel = False
                    sequential = 1
                else:
                    sequential += 1
            if tmp == before_word:
                if tmp not in exc:
                    ans = False
                    break
            before_word = tmp

            if sequential >= 3:
                ans = False
                break
            
    if not in_vowel:
        ans = False

    if ans:
        print(1)
    else:
        print(0)