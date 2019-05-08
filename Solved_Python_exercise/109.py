'''
Store a list of students and marks in a dictionary, and find the average marks obtained by a student.
'''
n = int(input('Enter the number of the students: '))
print("input the Name of the student followed by the marks.")
students_marks = dict()
for i in range(n):
    name, *marks_list = input().split()
    score = list(map(float,marks_list))
    students_marks[name] = score
query = input('Enter the name of the student whose avg who need to find.')
marks = students_marks[query]
print(format(sum(marks)/3,'.2f'))
