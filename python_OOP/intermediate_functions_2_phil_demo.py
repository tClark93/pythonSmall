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

# How would you change the value 10 in x to 15?  Once you're done x should then be [ [5,2,3], [15,8,9] ].  
x[1][0] = 15
# How would you change the last_name of the first student from 'Jordan' to "Bryant"?
students[0]['last_name'] = 'Bryant'
# For the sports_directory, how would you change 'Messi' to 'Andres'?
sports_directory['soccer'][0] = "Andres"
# For x, how would you change the value 20 to 30?

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
# Create a function that given a list of dictionaries, it loops through each dictionary in the list and prints each key and the associated value.  For example, given the following list:
def iterateDictionary(students): #the students up here has nothing to do with anything else
    for student in students:
        print(student)
        studentName = ''
        for key in students:
            studentName += key + ": " + student[key] + ', '
        print (studentName[len:(studentName) - 2])

# Create a function that given a list of dictionaries and a key name, it outputs the value stored in that key for each dictionary.  For example, iterateDictionary2('first_name', students) should output
def iterateFirst(iter:
    for student in iter:
        print(student[key])

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
# Create a function that prints the name of each location and also how many locations the Dojo currently has.  Have the function also print the name of each instructor and how many instructors the Dojo currently has.  For example, printDojoInfo(dojo) should output
def dojoBuilder(dojo_list):
    for dojo in dojo_list:
        print(len(dojo_list[dojo]), dojo.upper())
        for location in dojo_list[dojo]
        print(location)
dojoBuilder(dojo)