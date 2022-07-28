##### 클래스 #####
# 클래스(class)는 과자틀, 객체(object)는 과자
# 표현 = a는 객체이며, a 는 Cookie의 인스턴스이다.


class FourCal:#클래스 생성 방법, 아무것도 수행하지 않을 때는 pass라고 작성
    def __init__(self, first, second): # 생성자 메서드. 객체가 생성되는 시점에 자동으로 호출된다.
        self.first = first
        self.second = second # a = FourCal(a, b)로 값을 전달하여 객체를 만들 수 있다.
    def setdata(self, first, second): #클래스 안에 구현된 함수. 메서드(Method)라고 부른다.
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

# def setdata(self, first, second): --> 메서드의 매개변수
    # 첫 번째 매개변수 self에는 setdata를 호출한 객체 a가 자동으로 전달된다.
# self.first = first --> 메서드의 수행문
# self.second = second--> 메서드의 수행문
# a.setdata(4, 2)처럼 호출했을때
    # a.first = 4, a.second = 2
    # a객체에 객체변수 first가 생성되고 값 4가 저장된다.
    # 객체에 생성되는 객체만의 변수를 객체변수라고 부른다.

a = FourCal()
a.setdata(4, 2)
b = FourCal()
b.setdata(3, 7)
print(a.first)
print(b.first) #클래스로 만든 객체의 객체변수는 다른 객체와 상관없이 독립적인 값을 유지한다.
print(a.add())


##### 클래스의 상속 #####

class MoreFourCal(FourCal): #FourCal 클래스를 상속하는 MoreFourCal 클래스
    pass # FourCal의 모든 기능을 사용할 수 있어야 한다.

# 상속을 해야하는 이유: 기존 클래스 변경하지 않고 기능을 추가/변경
# 기존 클래스가 라이브러리 형태이거나 수정이 허용되지 않는 상황에 사용


##### 클래스 변수 #####

class Family:
    lastname = "김" #Family 클래스에 선언한 lastname이 클래스 변수.
    #클래스 안에 함수를 선언하는 것과 마찬가지로 변수를 선언하여 생성함.
    #클래스 이름.클래스 변수 로 사용할 수 있다.
    #클래스 변수는 모든 객체에 공유된다.