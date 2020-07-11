"""
https://programmers.co.kr/learn/courses/30/lessons/12922
문제 설명

길이가 n이고, 수박수박수박수....와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요. 예를들어 n이 4이면 수박수박을 리턴하고 3이라면 수박수를 리턴하면 됩니다.
제한 조건
n은 길이 10,000이하인 자연수입니다.
입출력 예
n	return
3	수박수
4	수박수박
"""


def solution(n):
    answer = ''
    # s = []
    w = ['수', '박']
    # for i in range(n):
    # s.append(w[i%2])
    s = [w[i % 2] for i in range(n)]
    answer = ''.join(s)
    return answer


"""
# other's solution

def water_melon(n):
    s = "수박" * n
    return s[:n]
"""
