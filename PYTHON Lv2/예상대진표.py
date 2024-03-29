# 토너먼트로 진행되는 경기일 때, a와 b가 만나게 된다면 그것은 몇 번째 라운드일까
# 이때, a,b는 항상 이긴다

def solution(n,a,b): #n: 총 참가자 수이며 모든 참가자는 1부터 번호 순이다
    if a<b: #참가자 a의 번호가 참가자 b의 번호보다 작게 배치
        arr=[a,b]
    else:
        tmp=a
        a=b
        b=tmp
        arr=[a,b]
    level=0
    while(True):
        if b%2==0 and b-1==a:# 종료 조건, [1,2], [3,4] 꼴로 될 때 종료
            return level+1
        a=int(a//2+a%2) # 시작: 8번 -> 4번 -> 2번..
        b=int(b//2+b%2) # 시작: 14번 -> 7번 -> 4번 ...
        #arr=[int(a//2+a%2),int(b//2+b%2)]
        arr=[a,b]
        level+=1 #그라운드 파악

solution(8,4,7)

# 결과
"""
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.00ms, 10.2MB)
테스트 3 〉	통과 (0.00ms, 10.3MB)
테스트 4 〉	통과 (0.00ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.1MB)
테스트 7 〉	통과 (0.01ms, 10.3MB)
테스트 8 〉	통과 (0.00ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.01ms, 10.3MB)
테스트 11 〉	통과 (0.00ms, 10.3MB)
테스트 12 〉	통과 (0.00ms, 10.2MB)
테스트 13 〉	통과 (0.01ms, 10.3MB)
테스트 14 〉	통과 (0.01ms, 10.2MB)
테스트 15 〉	통과 (0.00ms, 10.1MB)
테스트 16 〉	통과 (0.00ms, 10.3MB)
테스트 17 〉	통과 (0.01ms, 10.2MB)
테스트 18 〉	통과 (0.00ms, 10.2MB)
테스트 19 〉	통과 (0.01ms, 10.3MB)
테스트 20 〉	통과 (0.01ms, 10.2MB)
테스트 21 〉	통과 (0.01ms, 10.3MB)
테스트 22 〉	통과 (0.01ms, 10.3MB)
테스트 23 〉	통과 (0.01ms, 10.2MB)
테스트 24 〉	통과 (0.01ms, 10.3MB)
테스트 25 〉	통과 (0.00ms, 10.3MB)
테스트 26 〉	통과 (0.00ms, 10.3MB)
테스트 27 〉	통과 (0.01ms, 10.2MB)
테스트 28 〉	통과 (0.01ms, 10.2MB)
테스트 29 〉	통과 (0.01ms, 10.1MB)
테스트 30 〉	통과 (0.01ms, 10.3MB)
테스트 31 〉	통과 (0.01ms, 10.2MB)
테스트 32 〉	통과 (0.00ms, 10.3MB)
테스트 33 〉	통과 (0.01ms, 10.2MB)
테스트 34 〉	통과 (0.01ms, 10.3MB)
"""