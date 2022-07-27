# arr = [2, 1, 3]
# print(arr.index(5))
# arr.sort() # 1, 2, 3
# arr.sort(reverse=True) # 3, 2, 1
#
# students = [["000123", "name", 80, 70], ["000123", "name", 80, 70]]
# students.sort(key=lambda x:x[2])

# d = dict() # ㅋㅣ : 값
# dict["a"] = 2
# dict["b"] = 3
# sorted(d, key=lambda x:x[1])

# def swap(x, y):
#     temp = a
#     x = y
#     y = temp
#     return
#
# a = 1; b = 3
# x = a # x = 1
# a += 1 # a = 2
# x # 1
#
# a = "asDf"
# a.upper() # ASDF
#
# a, b = swap(a, b)
#
# print(a, b)

# Exception - class
# IndexError, ValueError, DivisionByZeroError - 상속받은 자식

class NegativeScoreError(Exception):
    pass

print("성적을 입력해주세요")
try:
    score = int(input())
    if score < 0:
        raise NegativeScoreError
except Exception:
    score = 0

# except NegativeScoreError:
#     print("성적은 양수여야 합니다")

print(score)