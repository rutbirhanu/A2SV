def gradingStudents(grades):
    for i in grades:
        x = 0

        if i < 38:
            pass
        else:

            while (i % 5 != 0):
                i+= 1
                x+=1

            if x < 3:
                y=i-x
                ind=grades.index(y)
                grades[ind]=i

            elif x > 3:
              pass
    return grades