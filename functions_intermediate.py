x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
# 1. Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ]
def change_x(some_list):
    some_list[1][0] = 15
    print(some_list)
change_x(x)
# 2. Change the last_name of the first student from 'Jordan' to 'Bryant'
def change_name(some_list):
    some_list[0]['last_name'] = 'Bryant'
    print(some_list)
change_name(students)

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# 3. In the sports_directory, change 'Messi' to 'Andres'
def sports(dict):
    (dict['soccer'][0]) = 'Andres'
    print(dict)
sports(sports_directory)

# 4. Change the value 20 in z to 30
def change_val(some_list):
    some_list[0]['y'] = 30
    print(some_list)
change_val(z)