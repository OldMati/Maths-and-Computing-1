# 02730341

students = []

# open the file and read the contents
with open('2024Final/ME1.txt') as f:
    data = f.readlines()

    n = len(data)

    # set i to the first line
    i = 0

    # loop over all lines
    while i < n:
        # save the name of the student as the first entry in the temporary array
        student = [data[i].rstrip()]

        # read the number of exams
        no_of_exams = int(data[i + 1])
        # set the index to the first exam
        i += 2

        # loop over all exams
        for exam in range(no_of_exams):
            # save exam mark to the temp array
            student.append(int(data[i + exam]))

        # compute average and add to the end of the temp array
        avg = sum(student[1:]) / no_of_exams
        student.append(avg)

        students.append(tuple(student))
        # set i to the next student
        i += no_of_exams

# sort the students by the highest average (student[-1])
students = sorted(students, key=lambda x: x[-1], reverse=True)

print('The student with the highest average mark: ', students[0][0])
