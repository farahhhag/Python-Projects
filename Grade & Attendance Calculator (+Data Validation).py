data_valid = False

while data_valid == False:
    grade1 = input("Enter the first grade: ")
    try:
        grade1 = float(grade1)
    except:
        print("Invalid input. Only numbers are accepted. Decimals should be separated with a dot.")
        continue
    if grade1 <0 or grade1 > 10:
        print("Grade should be in between 0 to 10")
        continue
    else:
        data_valid = True

data_valid = False

while data_valid == False:
    grade2 = input("Enter the second grade: ")
    try:
        grade2 = float(grade2)
    except:
        print("Invalid input. Only numbers are accepted. Decimals should be separated with a dot.")
        continue
    if grade2 <0 or grade2 > 10:
        print("Grade should be in between 0 to 10")
        continue
    else:
        data_valid = True
        
data_valid = False

while data_valid == False:
    total_class = input("Enter the number of total class: ")
    try:
        total_class = int(total_class)
    except:
        print("Invalid input. Only numbers are accepted.")
        continue
    if total_class <= 0:
        print("The number of total class can't be less than 0")
        continue
    else:
        data_valid = True

data_valid = False

while data_valid == False:
    absences = input("Enter the number of total absences: ")
    try:
        absences = int(absences)
    except:
        print("Invalid input. Only numbers are accepted.")
        continue
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
