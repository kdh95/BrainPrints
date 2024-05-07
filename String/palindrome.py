# 주어진 문자열이 팰린드롬인지 확인하라. 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.
# 대소문자 여부를 구분하지 않으며 영문자, 숫자만을 대상으로 한다.

# input : "A man, a plan, a cancel: Panama"
# output : true

# input : "race a car"
# output : false



def isPalindrome(self, s: str) -> bool:
    strs = []
    # 전처리 과정
    for char in s:
        if char.isalnum():# 해당 함수는 영문자, 숫자 여부를 판별하는 함수로, 이를 이용해 해당하는 문자만 추가한다.
            strs.append(char.lower()) # 대소문자를 구분하지 않으므로 lower()로 모두 소문자로 변환한다.
    # 팰린드롬 판별
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True


