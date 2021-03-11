print("BMI Calculator")

weight = float( input("Please enter your weight(kg): "))
height = float( input("Please enter your height(m): "))

bmi = (weight/(height*height))
       
if(bmi <= 18.5):
    print("Underweight")
elif(18.5 < bmi <= 24.9):
    print("Normal Weight")
elif(24.9 < bmi <= 29.9):
    print("Overweight")
else:
    print(bmi >= 30)




