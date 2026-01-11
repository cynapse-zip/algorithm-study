import sys

VOWELS = set("aeiou")

def acceptable(pw):
    has_vowel = False
    vowel_streak = 0
    cons_streak = 0
    prev = ""

    for char in pw:
        if char in VOWELS:
            has_vowel = True
            vowel_streak += 1
            cons_streak = 0
        else:
            cons_streak += 1
            vowel_streak = 0

        # 모음 3개 or 자음 3개 연속
        if vowel_streak >= 3 or cons_streak >= 3:
            return False

        # 같은 글자 연속 (ee, oo 제외)
        if prev == char and char != 'e' and char != 'o':
            return False
        
        # 지금 문자 -> 이전 문자로 저장
        prev = char

    return has_vowel

def solve():
    input = sys.stdin.readline
    while True:
        pw = input().strip()
        if pw == "end":
            break

        if acceptable(pw):
            print(f"<{pw}> is acceptable.")
        else:
            print(f"<{pw}> is not acceptable.")

solve()