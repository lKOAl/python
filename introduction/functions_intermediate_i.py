# 1 Update values in dictionaries and lists
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][1]=15
print(x) 

students[0]['last_name']="Bryant"
print(students)

sports_directory['soccer'][0]="Andres" #changing Messi to Andres
print(sports_directory)

z[0]['y']=30
print(z)

# 2 Iterate Through a list of Dictionaries
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
print(students[0])
print(students[1])
print(students[2])
print(students[3])

#iterateDictionary(students) 
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
#first_name - Michael, last_name - Jordan
#first_name - John, last_name - Rosales
#first_name - Mark, last_name - Guillen
#first_name - KB, last_name - Tonel

#3 Get values from a list of dictionaries 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterateDictionary(key, students):
 for s in students:
    print(s[key])
# calling the method with a key (first_name) and a list    
iterateDictionary('first_name', students)
# calling the method with a key (last_name) and a list
iterateDictionary('last_name', students)

# 4 Iterate through a dictionary with list values
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
print(f"{(len(dojo['locations']))}"' '"LOCATIONS")
def printInfo1(dojo):
    for i in dojo:
        x=dojo['locations']
    for y in x:
      print(y)
printInfo1(dojo)

print(f"{(len(dojo['instructors']))}"' '"INSTRUCTORS")
def printInfo2(dojo):

    for z in dojo:
        z=dojo['instructors']
    for m in z:
      print(m)
printInfo2(dojo)
