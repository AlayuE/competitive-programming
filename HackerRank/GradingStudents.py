def gradingStudents(grades):
    # Write your code here
    gradesList=[]
    for i in range(len(grades)):
        if grades[i]<38:
            gradesList.append(grades[i])
        elif (5-grades[i])%5 < 3:
            gradesList.append(grades[i]+((5-grades[i])%5))
        elif (5-grades[i])%5 >= 3:
            gradesList.append(grades[i])
    return gradesList
            
