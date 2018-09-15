# x = [ [5,2,3], [10,8,9] ] 
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15

students[0]['last_name'] = "Bryant"

sports_directory['soccer'][0] = "Andres"

z[0]['y'] = 30

# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]

for i in range (0,len(students),1):
  str = ""
  for key, val in students[i].items():
    str += " {} - {}, ".format(key,val)
  print(str)
  
for i in range (0,len(students),1):
  print(students[i]['first_name'])

# dojo = {
#    'location': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }

def DojoInfo(dojo):
  for i in dojo:
    print(len(dojo[i]),i.upper())
    for x in dojo[i]:
      print(x)

DojoInfo(dojo)