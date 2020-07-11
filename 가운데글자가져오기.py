"""
문제 설명

단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.
재한사항
s는 길이가 1 이상, 100이하인 스트링입니다.
"""


def solution(s):
    answer = ''
    div = int(len(s)/2)
    if len(s) % 2 == 0:
        answer = s[div-1:div+1]
    else:
        answer = s[div:div+1]
    return answer
    # return str[(len(str)-1)//2:len(str)//2+1]  # possibly "better" way?


# test
print(solution('powe'))  # 'ow'###
