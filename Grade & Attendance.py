grade1 = float( input("Enter the first grade: ") )
grade2 = float( input("Enter the second grade: ") )
absences = int( input("Enter the number of total absences: ") )
total_class = int( input("Enter the number of total class: ") )

avg_grade = (grade1+grade2) / 2
attendance = (total_class - absences) / total_class

print("Average Grade: ", round(avg_grade,2))
print("Attendance Rate: ", str( round((attendance*100),2))+"%")

if(avg_grade >= 6.0):
    if(attendance >= 0.8):
        print("The student has been approved.")
    else:
        print("The student has failed due to the Attendance Rate lower than 80%.")
elif(attendance >= 0.8):
    print("The student has failed due to the Average Grade lower than 6.0.")
else:
    print("The student has failed due to the Average Grade lower than 6.0 and Attendance Rate lower than 80%.")
