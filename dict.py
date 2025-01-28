students = {
'name':'Charan',
'age': 12,
'contact':162538449,
'marks' : [40,50,75,60] 
}                    
print(students)
print(students['name'])
print(students.get('marks'))

students['email'] = '123@gmail.com'
print(students.keys(),students.values())
del(students['contact'])
students['subjects'] = {'Eng': 97 ,'Math' : 99 , 'Sci' : 96}

for i in students:
    print(i)
for i in students.keys():
    print(i)
for i in students.values():
    print(i)        
for i in students:
    print(students[i]) 

print(students['subjects']['Eng'])