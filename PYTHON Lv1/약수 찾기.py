# 주어진 수의 약수들의 합을 구하라

import math

def solution(n):
    # 약수 구하기
    # []에 넣고, sum 예약어 사용
    # 약수 구하는 공식: 10, 1 2 5 10 / 5, 1 5 / 8, 1 2 4 8 / 9, 1 3 9 / 4: 1, 2, 4
    #24: 1 2 3 4 6 8 12 24
    #약수: 어떤 수를 나누어떨어지게 하는 수.
    # 1*24 = 2*12 = 3*8 = 4*6 
    # 1에서 n의 절반까지, 모든 인덱스를 n으로 나눈 값을 리스트에 저장하고,
    # 그 값을 다시 n으로 나눈 후의 몫을 리스트에 저장하면 어떨까?
    # 단 이 경우, n이 짝수냐 홀수냐로 나뉘겠지. 그래도 시간은 모든 수를 돌리는 것보단 빠를 듯.
    l=[]
   # n=input()
    n=int(n)
    n_half=int(math.sqrt(n))
    for i in range(1,n_half+1):
        if n%i==0:
            l.append(i)
    #print(l)
      #l에는 n의 루트값 기준으로 약수들이 들어가있음
      # 이제 n에서 l 각 값을 나누어 저장해야 함
    answer=[]
    for j in l:
        print(j)
        if n%j==0:
            answer.append(n//j)

    answer.sort()
    answer=sum(set(l+answer))
    return answer

"""
통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.02ms, 10.1MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.02ms, 10.2MB)
테스트 5 〉	통과 (0.02ms, 10MB)
테스트 6 〉	통과 (0.01ms, 10MB)
테스트 7 〉	통과 (0.01ms, 10.1MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.02ms, 10.2MB)
테스트 11 〉	통과 (0.02ms, 10.2MB)
테스트 12 〉	통과 (0.03ms, 10.1MB)
테스트 13 〉	통과 (0.02ms, 10.2MB)
테스트 14 〉	통과 (0.01ms, 10.2MB)
테스트 15 〉	통과 (0.01ms, 10.2MB)
테스트 16 〉	통과 (0.01ms, 10.1MB)
테스트 17 〉	통과 (0.01ms, 10.2MB)
"""




# 코드 수 줄이기
def solution(n):
    half=[i for i in range(1,int(n**0.5)+1) if n%i==0]
    last=[n//i for i in half if n%i==0]
    answer=sum(set(sorted(half+last)))
    return answer

"""
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.02ms, 10.1MB)
테스트 3 〉	통과 (0.03ms, 10.1MB)
테스트 4 〉	통과 (0.02ms, 10.3MB)
테스트 5 〉	통과 (0.02ms, 10.2MB)
테스트 6 〉	통과 (0.02ms, 10MB)
테스트 7 〉	통과 (0.02ms, 10.2MB)
테스트 8 〉	통과 (0.02ms, 10.3MB)
테스트 9 〉	통과 (0.02ms, 10.3MB)
테스트 10 〉	통과 (0.02ms, 10.1MB)
테스트 11 〉	통과 (0.02ms, 10.2MB)
테스트 12 〉	통과 (0.03ms, 10.1MB)
테스트 13 〉	통과 (0.02ms, 10.2MB)
테스트 14 〉	통과 (0.02ms, 10.3MB)
테스트 15 〉	통과 (0.81ms, 10.1MB)
테스트 16 〉	통과 (0.01ms, 10MB)
테스트 17 〉	통과 (0.02ms, 10.4MB)
"""
# runtime error남. remove써서 그런가
def solution(n):
    half=[i for i in range(1,int(n**0.5)+1) if n%i==0]
    last=[n//i for i in half if n%i==0]
    if n**0.5==int(n**0.5):
        last.remove(n**0.5)
    answer=sorted(half+last)
    return answer



def solution(n):
    half=[i for i in range(1,int(n**0.5)+1) if n%i==0]
    last=[n//i for i in half if n%i==0]
    answer=sum(set(sorted(half+last)))
    return answer