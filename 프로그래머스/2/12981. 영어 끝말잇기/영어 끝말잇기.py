def solution(n, words):
    used = set()  # 이미 나온 단어들

    for i in range(len(words)):
        word = words[i]

        # 다음 글자의 맨 첫번째 알파벳이 이전 글자 맨 끝 알파벳과 일치하지 않는 경우
        if i > 0 and words[i - 1][-1] != word[0]:   
            return [(i % n) + 1, (i // n) + 1]

        # 중복 단어 확인
        if word in used:
            return [(i % n) + 1, (i // n) + 1]

        used.add(word)

    # 끝까지 탈락자 없으면
    return [0, 0]