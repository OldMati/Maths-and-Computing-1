import pandas as pd


class Student():
    def __init__(self, CID, name, marks):
        self.CID = CID
        self.name = name
        self.marks = marks
        self.avg = None
        self.result = ''

    def average(self):
        if self.avg != None:
            return self.avg

        avg = 0
        for mark in self.marks:
            avg += mark
        
        self.avg = avg / len(self.marks)
        return self.avg
        
    def classify(self):
        if self.avg == None:
            self.avg = self.average()
        
        # 70-100: A
        # 60-70: B
        # 50-60: C
        # 40-50: D
        # 0-40: F

        if self.avg < 40:
            self.result = 'F'
        elif self.avg < 50 and self.avg >= 40:
            self.result = 'D'
        elif self.avg < 60 and self.avg >= 50:
            self.result = 'C'
        elif self.avg < 70 and self.avg >= 60:
            self.result = 'B'
        else:
            self.result = 'A'

        return self.result


class Cohort():
    def __init__(self, year, students):
        self.year = year
        self.students = students

    def best_student(self):
        best_stud = self.students[0]
        for student in self.students:
            if student.average() > best_stud.average():
                best_stud = student
        return best_stud
    
    def deans_list(self):
        num = len(self.students) // 10

        self.students.sort(key = lambda x: x.average(), reverse=True)
        deans_list = self.students[:num]

        return deans_list
            

class Registry():
    def __init__(self, department, enrollments):
        self.department = department
        self.enrollments = enrollments # list of cohorts

    def statistics(self, target_result):
        count = 0

        for enrollment in self.enrollments:
            for student in enrollment.students:

                if target_result == student.classify():
                    count += 1
        
        return count
    

ME = Registry('Mechanical Engineering',
              [
                  Cohort(2019, []),
                  Cohort(2020, []),
                  Cohort(2021, []),
                  Cohort(2022, [])
              ])

with open('Session7/Results.csv') as f:
    df = pd.read_csv(f)

df = df.iloc[1:]

subjects = df.columns.drop(['CID', 'Name'])

cols_conv = df.columns.drop('Name')
df[cols_conv] = df[cols_conv].astype(int)

for student in df.iloc:
    year = student['CID'] // 2000
    if year > 3:
        year = 3

    stud = Student(student['CID'], student['Name'], student[subjects])
    stud.average()
    ME.enrollments[year].students.append(stud)


for cohort in ME.enrollments:
    print(f'Cohort year: {cohort.year}, best student name: {cohort.best_student().name}')


deans_list = ME.enrollments[3].deans_list()
print('Cohort size: ', len(ME.enrollments[3].students))
print('DEANS LIST: ')
for student in deans_list:
    print(student.name)

for student in ME.enrollments[0].students:
    #result = 
    print(f'Name: {student.name}, result: {student.classify()}, avg: {int(student.average())}')