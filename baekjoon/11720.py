a = int(input())
b = input()


c = []

for i in range(a):
    c.append(int(b[i]))
    if len(c) == a:
        print(sum(c))
