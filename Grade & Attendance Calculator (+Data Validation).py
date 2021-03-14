data_valid = False

while data_valid == False:
    grade1 = float( input("Enter the first grade: ") )
    if grade1 <0 or grade1 > 10:
        print("Grade should be in between 0 to 10")
        continue
    else:
        data_valid = True

data_valid = False

while data_valid == False:
    grade2 = float( input("Enter the second grade: ") )
    if grade2 <0 or grade2 > 10:
        print("Grade should be in between 0 to 10")
        continue
    else:
        data_valid = True
        
data_valid = False

while data_valid == False:
    total_class = int( input("Enter the number of total class: ") )
    if total_class <= 0:
        print("The number of total class can't be less than 0")
        continue
    else:
        data_valid = True

data_valid = False

while data_valid == False:
    absences = int( input("Enter the number of total absences: ") )
    if absences <=0 or absences > total_class:
        print("The number of absences can't be less than 0 or greater than the number of total classes")
        continue
    else:
        data_valid = True


avg_grade = (grade1 + grade2) / 2
attendance = (total_class - absences) / total_class

print("Average Grade:", round(avg_grade, 2))
print("Attendance Rate:", str(round((attendance * 100),2))+"%")

if (avg_grade >= 6.0 and attendance >= 0.8):
    print("The student has been approved")
elif(avg_grade < 6.0 and attendance < 0.8):
    print("The student has failed because the attendance rate is lower than 80% and the average grade is lower than 6.0")
elif(attendance >= 0.8):
    print("The student has failed because the average grade is lower than 6.0")
else:
     print("The student has failed because the attendance rate is lower than 80%")
