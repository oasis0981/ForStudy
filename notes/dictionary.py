##### 딕셔너리 #####

# key와 value를 한 쌍으로 갖는 자료형
# 리스트나 튜플처럼 순차적으로 해당 요솟값을 구하지 않고, Key를 통해 Value를 얻는다.
# 기본 형태: {Key1:Value1, Key2:Value2, Key3:Value3, ...}
# Key에는 변하지 않는 값, Value에는 변하는 값/변하지 않는 값 모두 사용 가능

## 예시
dic = {'name':'pey', 'phone':'01025383839', 'birth':'1116'}
a = {'a':[1,2,3]} #Value에 리스트도 넣을 수 있다.

b = {1:'a'}
b[2] = 'b' # 딕셔너리 쌍 추가
print(b)


##### 딕셔너리에서 Key 사용해 Value 얻기 #####
grade = {'pey':10, 'amy':99}
print(grade['pey'])


##### Key 리스트 만들기(Keys) #####
print(list(dic.keys())) #리스트로 변환
print(dic.values())
print(dic.items()) #key와 value의 쌍을 튜플로 묶은 값을 반환

