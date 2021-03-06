"""
사용자로부터 신규 id를 받고, 아래의 조건에 맞춰 변환시키기

1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다. #바로 처리 가능
2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다. #if로만 가능
3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다. #if로만 가능
4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다. #if로만 가능
5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다. #if로만 가능
6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다. #if로만 가능
     만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.

"""

# 틀린 방법이지만, replace함수에 대해 새로 알게 된 것이 있어서
def solution(new_id):
    
    """
    생략
    """
    # 연속된 . 이 있으면 이를 하나의 .으로 압축(?) 하기 위한 부분이다.
    # 하나씩 순차적으로 돌고, 바로 뒷 문자열과 비교한 후 .이 있으면 교체하도록 하려 했다.
    #이의 결과는, 가장 앞 부분. 즉, 앞부분을 제외한 곳에 연속된 .이 있어도 이는 if문에서 읽지를 못 한다 ==> 
    # find함수는 가장 앞에 것만 부르기 때문이다. 즉, find함수로 처음에 있는 .의 위치만 찾아내기 때문에, 재귀로 호출해도 똑같은 결과가 나타난다
    if new_id[new_id.find('.')+1]=='.':
        print('pass1.find()의 결과',new_id.find('.'))
        new_id=new_id.replace('.','',1) #바꿀 횟수!!!!!!!!!!!
        solution(new_id) #재귀함수로 3단계 다시 거르기 위해서. ==>

    #하나 새로 알게 된 방법은, replace에 바꿀 횟수를 지정할 수 있다는 것이다. 예를 들어,
    name= "ABC DEF ABC ABC DEF def"
    result= name.replace("ABC", "123",2)
    # result의 결과는: 123 DEF 123 ABC DEF def 이다. 즉 두 번만 바뀐다
    # 알다 싶이, 횟수를 지정하지 않으면 전부 바뀐다
    """
    생략
    """
    return new_id

#정답
def solution(new_id):
    #1단계
    new_id=new_id.lower() # 모든 문자를 소문자로 변환
    #2단계
    tmp='' # 2단계
    for i in range(len(new_id)):
        if (new_id[i].isalpha()) or new_id[i] in ['_','-','.'] or (new_id[i].isdigit()):
            tmp+=new_id[i]
            
    new_id=tmp # 다시 복귀
    #print(new_id)
    #3단계
    #***************여기 주목! 연속된 문자를 치환하는 방법!
    while '..' in new_id:
        new_id=new_id.replace('..','.')

    #4단계 
    if new_id[0]=='.': new_id=new_id[1:] if len(new_id)>1 else '.'
    if new_id[-1:]=='.':new_id=new_id[:-1]

    # 5단계
    if new_id == '': new_id='a'
    #6단계
    if len(new_id)>=16: new_id=new_id[:15] 
    if new_id[-1:]=='.':new_id=new_id[:-1]
    # 7단계
    
    if len(new_id)<=2: 
        adding=3-len(new_id)
        new_id=new_id+new_id[-1:]*adding
    
        
    return new_id