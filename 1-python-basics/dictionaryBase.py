#Dictionary creation
students = {
    'Nishith' : 85,
    'Bob' : 86,
    'Tom': 77
}

#Adding a student in to dictionary
students['Moon']= 78
#Updating info
students['Nishith']= 88
print(students)

#Deleting
del students['Moon']
print(students)

#Looping through dictionary
for name, score in students.items():
    print(f'{name} scored {score}')

#Finding average
average = sum(students.values())/len(students)
print(f'Average score is {average:.2f}')

#Finding best score
top_student = max(students, key=students.get)
print(f'{top_student} gets the highest score of {students[top_student]}')