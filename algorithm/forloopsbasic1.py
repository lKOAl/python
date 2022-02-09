"""def loop_basic(x = 150):
    while x >= 0:
        print(x)
        x -= 1
        print(*range(5, 1001, 5)) 
loop_basic(150)"""


for i in range(151):
    print(i)

for i in range (0, 1001, 5):
    print(i)

"""help with #3 counting, the dojo way"""
for i in range(101):
    print(i)
    if i % 5 == 0:
        print("Coding")
    if i % 10 == 0:
        print("Dojo")

for i in range(501):
    if(i % 2 != 0):
        print(i)

for i in range(2018, 0, -4):
    print(i)

lowNum = 2
highNum = 9
mult = 3

for i in range(lowNum, highNum + 1):
    if i % mult == 0:
        print(i)