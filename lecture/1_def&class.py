# # 1번 - 거꾸로별
# N = int(input())
# for i in range(N+1, 0, -1):
#     print("*" * i)
#     # range(시작, 끝, 증감)
#
# # 2번 - 평균 점수
# students = []
# for i in range(5):
#     students.append(max(40, int(input())))
# print(sum(students)/5)
#
# result = 0
# for i in range(5):
#     result += max(40, int(input()))
# print(result/5)
#
#
# # 3. 숫자의 합
# a = int(input())
# b = input()
#
# c = 0
# for i in range(a):
#     c += (int(b[i]))
# print(c)

# 수업

# for i in range(100):
#     if j == 3:
#         continue
#     j += 1
# break, continue는 while, for 등 반복문에서 다 사용가능

def add(a, b):
    return a + b

c = add(1, 3)

# 절차지향
# C

# 객체지향
# Java
# -> class
#
class Human:
    race = "orange"
    def __init__(self):
        print("born!")

    def run(self):
        print("run!")
    def eat(self):
        print("eat")

human1 = Human()
human1.height = 180
human1.weight = 90

class Nurse(Human):
    def __init__(self): #생성자 메서드.
        print("born nurse!")

    def run(self):
        super().run()
        print("nurse run!")
    def nursing(self):
        print("nursing")

nurse = Nurse()
nurse.eat()
nurse.run()

