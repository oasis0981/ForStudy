
print("=" * 50)
print("My Program")
print("=" * 50)

a = "life is too short"
print(len(a)) #글자수세기



#인덱싱 = 가리킨다, 슬라이싱 = 잘라낸다

a = "Life is too short, You need phython"
print(a[3]) #인덱싱, 문자열 안의 특정한 값을 뽑아냄
print(a[0:4]) #슬라이싱, 0~3 문자 뽑아냄. **마지막 수는 제외함 주의
print(a[:]) #슬라이싱, 처음부터 끝까지
print(a[19:-7]) #슬라이싱, 19부터 -8까지.


b = "20010331Rainy"
date = b[:8]
weather = b[8:]
print(date)
print(weather)

# 문자열 요소 바꿀때 --> 문자열 자료형은 요솟값을 변경할 수 없으므로 immutable 자료형이라고도 함
# 하지만 슬라이싱 기법으로 바꾸기 가능하다.
c = "Pithon"
print(c[:1] + 'y' + c[2:])


# 문자열 포매팅
print("I eat %d apples." %3) #정수
print("I eat %s apples." %'five') #문자열
number = 3
print("I eat %d apples." %number) #숫자값 변수
day = "three"
print("I eat %d apples, so I was sick for %s days." %(number, day))