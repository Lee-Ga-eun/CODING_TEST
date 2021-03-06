# strings가 ["sun", "bed", "car"]이고 n이 1이면 
# 각 단어의 인덱스 1의 문자 "u", "e", "a"로 strings를 오름차순 정렬

# 풀이1
import collections

def solution(strings, n):
    dicT={}
    for k, v in enumerate(strings): # n을 뽑아낸 딕셔너리 생성
        dicT[v[n]]=k
    print(dicT)
    ans=collections.OrderedDict(sorted(dicT.items())) # 문자대로 정렬
    print(ans)
    answer=[strings[i] for i in ans.values()]
    return answer
    
     ## 딕셔너리는 순서가 없다. 따라서 OrderedDict를 통해 순서를 정해줘야 한다
     ## 키는 중복될 수 없다
    
# 풀이2

def solution2(strings, n):
    answer=sorted(sorted(strings), key=lambda x:x[n])
    return answer


#풀이3
from operator import itemgetter, attrgetter, methodcaller

def solution(strings, n):
    return sorted(sorted(strings), key=itemgetter(n))


### lambda
# lambda는 anonymous function 이다
f= lambda: 'foo'
f # 결과: <function __main__.<lambda>()>
f() # 결과: 'foo'

def lowercased(word): return word.lower()
sorted(['Some', 'words', 'sort', 'differently'], key=lowercased)

sorted(['Some', 'words', 'sort','differently'], key=lambda x: x[3])