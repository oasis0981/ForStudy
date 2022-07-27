i = 0
while i < 5:
    i = i + 1
    print("*" * i)

N = int(input())
for i in reversed(range(N+1)):
    print ( "*" * i )

WS = int(input())
SH = int(input())
SG = int(input())
SS = int(input())
GS = int(input())

for score in range(101):
    if WS < 40:
        WS = 40
    if SH < 40:
        SH = 40
    if SG < 40:
        SG = 40
    if SS < 40:
        SS = 40
    if GS < 40:
        GS = 40

total = WS + SH + SG + SS + GS
average = int(total/5)
print(average)