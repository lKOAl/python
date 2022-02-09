#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
# predication: 5

#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
# prediction: error

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
# prediction: 5

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
# prediction: 5 , 10 
# only printed 5

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
# 5, nothing

#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
# nothing because we didnt assign value to b and c

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
# prediction 7
# printed 25

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
# prediction 100 and 10 because 100 is not < 10

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3)) # 2>3 print 7
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3)) #5>3 else print 14
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3)) # (2>3 print 7) + (5>3 print 14) 21=7+14
# 7, 14, 21

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
# print 8

#11
b = 500
print(b) #print 500
def foobar():
    b = 300
    print(b)
print(b) #500
foobar() #300
print(b) #300


#12
b = 500 
print(b) #print 500
def foobar():
    b = 300
    print(b)
    return b
print(b) #500
foobar() #function is call #print 300
print(b) # print 500


#13
b = 500
print(b) # print 500
def foobar():
    b = 300
    print(b)
    return b
print(b) #return b so instead of print 300 it prints 500
b=foobar() #defining foobar in b print 300
print(b) # 300


#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
# 1, 2, 3

#15
def foo():
    print(1) # 1
    x = bar() #bar print 3 in line 131
    print(x) 
    return 10
def bar():
    print(3) #print 3
    return 5 # 5
y = foo()
print(y) # foo(y) return 10
# 1, 3, 5, 10