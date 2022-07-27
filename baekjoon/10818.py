# 10818번

a = int(input())
b = input().split()

c = []
for i in range(a):
    c.append(int(b[i]))

print(min(c), max(c))
