##### 리스트 정렬: sort와 sorted의 차이점 #####

# sort 형식: 리스트명.sort()  --> 리스트 원본 값을 직접 수정
# sorted 형식: sorted(리스트명) --> 리스트 원본 값은 그대로 두고 정렬 값을 반환


# sort
a = [2, 3, 1]
a.sort(reverse=True)
print(a)


# sorted
b = [ 7, 3, 5]
c = sorted(b)
print(b)
print(c)


##### sort에서 lambda 사용법 #####
students = [["000123", "name", 100, 70], ["000453", "name", 80, 90]]
students.sort(key=lambda x:x[2]) #리스트 두번째 값을 기준으로 정렬
print(students)