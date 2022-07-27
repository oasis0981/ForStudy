# 브론즈 3
# 2588번

a = int(input())
b = input()

second_number = []
for i in range(3):
    second_number.append(int(b[i]))

for j in range(2, -1, -1):
    print(a * second_number[j])

print(a * int(b))