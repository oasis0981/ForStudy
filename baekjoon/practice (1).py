f = open("C:/doit/students.txt", "r")
lines = f.readlines()
for line in lines:
    line = line.strip()
    print(line)
f.close()
