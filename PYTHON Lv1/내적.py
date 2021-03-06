"""
길이가 같은 두 1치원 정수 배열 a,b
a와 b의 내적은 a[0]*b[0] + a[1]*b[1]....+a[n-1]*b[n-1]
"""

# 시간이 빠른 순으로

def solution(a, b):
    return sum(x*y for (x,y) in zip(a,b))

    """
    테스트 1 〉	통과 (0.07ms, 10.3MB)
    테스트 2 〉	통과 (0.01ms, 10.2MB)
    테스트 3 〉	통과 (0.01ms, 10.3MB)
    테스트 4 〉	통과 (0.01ms, 10.2MB)
    테스트 5 〉	통과 (0.01ms, 10.1MB)
    테스트 6 〉	통과 (0.04ms, 10.2MB)
    테스트 7 〉	통과 (0.06ms, 10.2MB)
    테스트 8 〉	통과 (0.07ms, 10.2MB)
    테스트 9 〉	통과 (0.07ms, 10.3MB)
    """

def solution(a, b):
    answer=0
    for i in range(len(a)):
        answer+=a[i]*b[i]
    """
    테스트 1 〉	통과 (0.09ms, 10.1MB)
    테스트 2 〉	통과 (0.01ms, 10.1MB)
    테스트 3 〉	통과 (0.01ms, 10.1MB)
    테스트 4 〉	통과 (0.01ms, 10.2MB)
    테스트 5 〉	통과 (0.01ms, 10.1MB)
    테스트 6 〉	통과 (0.05ms, 10.2MB)
    테스트 7 〉	통과 (0.07ms, 10.4MB)
    테스트 8 〉	통과 (0.09ms, 10.1MB)
    테스트 9 〉	통과 (0.09ms, 10.2MB)
    """

def solution(a, b):

    return sum([a[i]*b[i] for i in range(len(a))])
    """
    테스트 1 〉	통과 (0.11ms, 10MB)
    테스트 2 〉	통과 (0.01ms, 10.1MB)
    테스트 3 〉	통과 (0.01ms, 10.3MB)
    테스트 4 〉	통과 (0.01ms, 10.2MB)
    테스트 5 〉	통과 (0.01ms, 10.1MB)
    테스트 6 〉	통과 (0.06ms, 10.2MB)
    테스트 7 〉	통과 (0.09ms, 10.1MB)
    테스트 8 〉	통과 (0.10ms, 10.4MB)
    테스트 9 〉	통과 (0.10ms, 10.3MB)
    """


# lambda를 이용한
def solution(a, b):
    return sum(map(lambda i: a[i]*b[i], range(len(a))))

# anonymous
solution = lambda x, y: sum(a*b for a, b in zip(x, y))
