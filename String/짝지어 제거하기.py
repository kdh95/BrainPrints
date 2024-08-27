# 프로그래머스 문제 Level-2
# 짝지어 제거하기


s = "baabaa"
def remove(s):
    while len(s) > 1:
        makeList = list(s)
        for i in range(len(makeList)-1):
            if makeList[i] == makeList[i + 1]:
                makeList[i] = makeList[i + 1] = '' # 빈 값으로 변경

        new_s = ''.join(s)
        if len(s) == len(new_s): break
        s = new_s

    return 1 if len(s) == 0 else 0


remove(s)
